'''

    This script transforms the SGV Metadata export to csv files,
    that can be easily imported into Omeka with the help of the
    BulkImport module.

    TODO: Property Comments are skipped for now, as their ontological
    status isn't clear.

'''
import argparse, csv, json, os, re, requests, urllib
from shapely.geometry import shape
from lxml import etree as et

with open('swiss_boundaries/swissBOUNDARIES3D_1_3_TLM_BEZIRKSGEBIET.geojson') as f:
    districts = json.load(f)
with open('swiss_boundaries/swissBOUNDARIES3D_1_3_TLM_HOHEITSGEBIET.geojson') as f:
    territories = json.load(f)

def main():

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    data = []

    column_count = 219
    buffer_row = []

    current_parent = []
    current_index  = -1

    print('Parsing CSV file into data structure.')

    with open (filename) as f:
        datareader = csv.reader(f, delimiter=';', quotechar='"')

        for row in datareader:

            if current_index % 100000 == 0:
                print('Parsed '+str(current_index)+' lines.')
            current_index += 1

            if(row[0] != ''):

                # reset object
                if current_index > 0:
                    data.append(current_parent)
                    current_parent = []

            current_parent.append(row)

    # main objects
    agents = []
    agents_header = [
        'schema:identifier',                        # id
        'schema:name',                              # hasName
        'schema:description ^^html',                # hasDescription
        'schema:relatedTo',                         # hasFamily
        'schema:jobTitle',                          # hasJob
        'schema:birthDate ^^timestamp ; interval',  # hasBirthdate
        'schema:birthPlace ^^item',                 # hasBirthplace
        'schema:deathDate ^^timestamp ; interval',  # hasDeathdate
        'schema:deathPlace ^^item',                 # hasDeathplace
        'schema:comment',                           # hasComment, hasLiterature
    ]

    concepts = []
    concepts_header = [
        'schema:identifier',            #id
        'schema:name',                  #hasPrefLabel
        'schema:description ^^html',    #hasDescription
    ]

    albums = []

    collections = []
    collections_header = [
        'schema:identifier',                        # hasSignature
        'schema:name',                              # hasTitle
        'schema:temporal ^^timestamp ; interval',   # hasDate
        'schema:creator ^^item',                    # hasCreator
        'schema:keywords',                          # hasKeywords
        'schema:about ^^item',                      # hasConcept
        'schema:comment',                           # hasComment, hasLiterature
        'schema:copyrightHolder ^^item',            # hasCopyright
        'schema:description ^^html',                # hasDescription
        'schema:spatial',                           # hasArchiveLocation
        # '',                     # hasIndexing
        # '',                     # hasRestoration
        #'schema:workExample',   # hasDefault_image
        #'schema:workExample',   # hasEmbedded_video
    ]

    objects = []
    objects_header = [
        'schema:identifier',                        # hasSignature, hasOldnr
        'schema:name',                              # hasTitle
        'schema:temporal ^^timestamp ; interval',   # hasDate
        'schema:location ^^item',                   # hasPlace
        'schema:creator ^^item',                    # hasCreator
        'edm:isRepresentationOf ^^item',            # isRepresentationOf schould be edm: not schema:
        'schema:keywords',                          # hasKeywords
        'schema:about ^^item',                      # hasConcept
        'schema:comment',                           # hasComment
        'schema:isPartOf',                          # hasIn_collection, hasPart_of
        'schema:material ^^item',                   # hasObjectType
        'schema:artMedium ^^item',                  # hasMedium
        'schema:size ^^item',                       # hasFormat
        'schema:copyrightHolder ^^item',            # hasCopyright
        'schema:image ^^uri',                       # iiif image
        'schema:geo ^^geometry:geography:coordinates',
        # 'edm:isRelatedTo',                        # hasRef_img
        # 'edm:isRelatedTo',                        # hasverso
    ]

    # secondary objects
    places = []         # schema:location
    places_header = [
        'schema:identifier',
        'schema:name',
        'schema:latitude',
        'schema:longitude',
        'schema:elevation',
        'pia:population',
        'schema:geo ^^geometry:geography:coordinates',
        'pia:geometry ^^geometry',
        'schema:url ^^uri',
    ]

    # list objects
    lists_header = [
        'schema:identifier',
        'schema:name'
    ]
    media = []   # schema:artMedium
    medium_list = []
    sizes = []        # schema:size
    size_list = []
    materials = []   # schema:material
    material_list = []

    print('Populating lists')
    with open('sgv.json') as f:
        lists = json.load(f)
    
    for l in lists['project']['lists']:
        if l['name'] == 'format':
            size_list = extract_list(l, 'nodes')
        if l['name'] == 'technology':
            medium_list = extract_list(l, 'nodes')
        if l['name'] == 'objecttype':
            material_list = extract_list(l, 'nodes')

    for l in size_list:
        for p in l:
            sizes.append(
                {
                    'schema:identifier': p['name'],
                    'schema:name': p['labels']['de']
                }
            )
    for l in medium_list:
        for p in l:
            media.append(
                {
                    'schema:identifier': p['name'],
                    'schema:name': p['labels']['de']
                }
            )
    for l in material_list:
        for p in l:
            materials.append(
                {
                    'schema:identifier': p['name'],
                    'schema:name': p['labels']['de']
                }
            )

    obj_count = 1

    for obj in data:

        obj_count += 1
        print('Worked through '+str(obj_count)+' of '+str(len(data))+' objects.')

        if obj[0][1] == ':Agent':

            agent = {
                'schema:identifier': obj[0][0],
                'schema:name': '',
                'schema:description ^^html': '',
                'schema:relatedTo': '',
                'schema:jobTitle': '',
                'schema:birthDate ^^timestamp ; interval': '',
                'schema:birthPlace ^^item': '',
                'schema:deathDate ^^timestamp ; interval': '',
                'schema:deathPlace ^^item': '',
                'schema:comment': '',
            }

            comments = []

            for prop in obj:
                value = merge_values(prop)

                if prop[6] == 'hasName':
                    agent['schema:name'] = value
                elif prop[6] == 'hasDescription':
                    agent['schema:description ^^html'] = value
                elif prop[6] == 'hasFamily':
                    agent['schema:relatedTo'] = value
                elif prop[6] == 'hasJobTitle':
                    agent['schema:jobTitle'] = value
                elif prop[6] == 'hasBirthDate':
                    agent['schema:birthDate ^^timestamp ; interval'] = clean_date(value)
                elif prop[6] == 'hasBirthPlace':
                    if not any(place['schema:identifier'] == 'place_'+prop[9] for place in places):
                        place = add_place(prop[9])
                        if place:
                            places.append(place)
                    agent['schema:birthPlace ^^item'] = 'place_'+prop[9]
                elif prop[6] == 'hasDeathDate':
                    agent['schema:deathDate ^^timestamp ; interval'] = clean_date(value)
                elif prop[6] == 'hasDeathPlace':
                    if not any(place['schema:identifier'] == 'place_'+prop[9] for place in places):
                        place = add_place(prop[9])
                        if place:
                            places.append(place)
                    agent['schema:deathPlace ^^item'] = 'place_'+prop[9]
                elif prop[6] == 'hasComment':
                    comments.append(value)
                elif prop[6] == 'hasLiterature':
                    comments.append(value)
            
            agent['schema:comment'] = '|'.join(comments)
            agents.append(agent)

        if obj[0][1] == ':Concept':

            concept = {
                'schema:identifier': obj[0][0],
                'schema:name': '',
                'schema:description ^^html': '',
            }

            for prop in obj:
                value = merge_values(prop)

                if prop[6] == 'hasName':
                    concept['schema:name'] = value
                elif prop[6] == 'hasDescription':
                    concept['schema:description ^^html'] = value
            
            concepts.append(concept)

        if obj[0][1] == ':Collection': #  and obj[0][2] in ['SGV_10', 'SGV_12']

            collection = {
                'schema:identifier': '',
                'schema:name': '',
                'schema:temporal ^^timestamp ; interval': '',
                'schema:creator ^^item': '',
                'schema:keywords': '',
                'schema:about ^^item': '',
                'schema:comment': '',
                'schema:copyrightHolder ^^item': '',
                'schema:description ^^html': '',
                'schema:spatial': '',
            }

            comments = []

            for prop in obj:
                value = merge_values(prop)

                if prop[6] == 'hasSignature':
                    collection['schema:identifier'] = value
                elif prop[6] == 'hasTitle':
                    collection['schema:name'] = value
                elif prop[6] == 'hasDate':
                    collection['schema:temporal ^^timestamp ; interval'] = clean_date(value)
                elif prop[6] == 'hasCreator':
                    collection['schema:creator ^^item'] = value
                elif prop[6] == 'hasKeywords':
                    collection['schema:keywords'] = value
                elif prop[6] == 'hasConcept':
                    collection['schema:about ^^item'] = value
                elif prop[6] == 'hasComment':
                    comments.append(value)
                elif prop[6] == 'hasCopyrightHolder':
                    collection['schema:copyrightHolder ^^item'] = value
                elif prop[6] == 'hasDescription':
                    collection['schema:description ^^html'] = value
                elif prop[6] == 'hasLiterature':
                    comments.append(value)
                elif prop[6] == 'hasArchiveLocation':
                    collection['schema:spatial'] = value
            
            collection['schema:comment'] = '|'.join(comments)
            collections.append(collection)

        if obj[0][1] == ':Object' and any(x in obj[0][2] for x in ['SGV_10', 'SGV_12']):

            objct = {
                'schema:identifier': '',
                'schema:name': '',
                'schema:temporal ^^timestamp ; interval': '',
                'schema:location ^^item': '',
                'schema:creator ^^item': '',
                'edm:isRepresentationOf ^^item': '',
                'schema:keywords': '',
                'schema:about ^^item': '',
                'schema:comment': '',
                'schema:isPartOf': '',
                'schema:material ^^item': '',
                'schema:artMedium ^^item': '',
                'schema:size ^^item': '',
                'schema:copyrightHolder ^^item': '',
                'schema:image ^^uri': '',
                'schema:geo ^^geometry:geography:coordinates': '',
            }

            ids = []
            partof = []

            for prop in obj:
                value = merge_values(prop)

                if prop[6] == 'hasSignature':
                    ids.append(value)
                elif prop[6] == 'hasTitle':
                    objct['schema:name'] = value
                elif prop[6] == 'hasDate':
                    objct['schema:temporal ^^timestamp ; interval'] = clean_date(value)
                elif prop[6] == 'hasPlace':
                    if not any(place['schema:identifier'] == 'place_'+prop[9] for place in places):
                        place = add_place(prop[9])
                        if place:
                            places.append(place)
                            objct['schema:geo ^^geometry:geography:coordinates'] = place['schema:geo ^^geometry:geography:coordinates']
                    else:
                        for place in places:
                            if place['schema:identifier'] == 'place_'+prop[9]:
                                objct['schema:geo ^^geometry:geography:coordinates'] = place['schema:geo ^^geometry:geography:coordinates']
                    objct['schema:location ^^item'] = 'place_'+prop[9]
                elif prop[6] == 'hasCreator':
                    objct['schema:creator ^^item'] = value
                elif prop[6] == 'isRepresentationOf':
                    objct['edm:isRepresentationOf ^^item'] = value
                elif prop[6] == 'hasKeywords':
                    objct['schema:keywords'] = value
                elif prop[6] == 'hasConcept':
                    objct['schema:about ^^item'] = value
                elif prop[6] == 'hasComment':
                    objct['schema:comment'] = value
                elif prop[6] == 'hasOldnr':
                    ids.append(value)
                elif prop[6] == 'hasCollection':
                    partof.append(value)
                elif prop[6] == 'isPartOfAlbum':
                    partof.append(value)
                elif prop[6] == 'hasObjectType':
                    objct['schema:material ^^item'] = value
                elif prop[6] == 'hasMedium':
                    objct['schema:artMedium ^^item'] = value
                elif prop[6] == 'hasFormat':
                    objct['schema:size ^^item'] = value
                elif prop[6] == 'hasCopyrightHolder ^^item':
                    objct['schema:copyrightHolder ^^item'] = value

            collection = 'SGV_10'

            if 'SGV_12' in obj[0][2]:
                collection = 'SGV_12'

            objct['schema:image ^^uri'] = 'http://sipi.participatory-archives.ch/'+collection+'/'+obj[0][2]+'.jp2'
            
            objct['schema:identifier'] = '|'.join(ids)
            objct['schema:isPartOf'] = '|'.join(partof)
            objects.append(objct)

    with open('agents.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = agents_header, delimiter=';')
        writer.writeheader()
        writer.writerows(agents)

    with open('concepts.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = concepts_header, delimiter=';')
        writer.writeheader()
        writer.writerows(concepts)

    with open('collections.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = collections_header, delimiter=';')
        writer.writeheader()
        writer.writerows(collections)

    with open('objects.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = objects_header, delimiter=';')
        writer.writeheader()
        writer.writerows(objects)

    with open('places.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = places_header, delimiter=';')
        writer.writeheader()
        writer.writerows(places)

    with open('sizes.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = lists_header, delimiter=';')
        writer.writeheader()
        writer.writerows(sizes)

    with open('media.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = lists_header, delimiter=';')
        writer.writeheader()
        writer.writerows(media)

    with open('materials.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = lists_header, delimiter=';')
        writer.writeheader()
        writer.writerows(materials)

def merge_values(row, prep = ''):
    values = []
    i = 9

    try:
        while row[i] != '':
            values.append((prep+row[i]))
            i += 5
    except:
        print('wanted to much…')
    
    return '|'.join(values)

def extract_list(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                if k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def add_place(id):

    geonames_data = resolve_geonames(id)

    if geonames_data:
        geonames_id = geonames_data.findtext('geonameId', default = '')

        label = geonames_data.findtext('name', default = '')
        uris = [
            'https://www.salsah.org/api/geonames/{}?reqtype=info'.format(id),
            'http://sws.geonames.org/'+geonames_id
            ]

        geometry = ''
        geonames_division_level = '1'

        for alternatename in geonames_data.iterfind('alternateName'):
            if alternatename.get('lang') == 'link' and 'en.wikipedia.org' in alternatename.text:
                uris.append(alternatename.text)
            if alternatename.get('isPreferredName') and alternatename.get('lang') == 'de':
                label = alternatename.text

        if geonames_data.findtext('adminCode2', default = 0):
            geonames_division_level = '2'
        if geonames_data.findtext('adminCode3', default = 0):
            geonames_division_level = '3'

        if geonames_division_level == '2':
            for feature in districts['features']:
                if str(feature['properties']['BEZIRKSNUM']) == str(geonames_data.findtext('adminCode2')):
                    geometry = shape(feature['geometry']).wkt

        if geonames_division_level == '3':
            for feature in territories['features']:
                if str(feature['properties']['BFS_NUMMER']) == str(geonames_data.findtext('adminCode3')):
                    geometry = shape(feature['geometry']).wkt
        
        return {
            'schema:identifier': 'place_'+id,
            'schema:name': label,
            'schema:geo ^^geometry:geography:coordinates': str(geonames_data.findtext('lat', default = 0))
                +','+str(geonames_data.findtext('lng', default = 0)),
            'schema:elevation': geonames_data.findtext('elevation', default = 0),
            'pia:population': geonames_data.findtext('population', default = 0),
            'pia:geometry ^^geometry': geometry,
            'schema:url ^^uri': '|'.join(uris)
        }
    
    else:

        return None

def resolve_geonames(id):
    geonames_dir = 'geonames'
    if not os.path.exists(geonames_dir):
        os.makedirs(geonames_dir)
    
    geonames_salsah_file = '/'.join((geonames_dir, (id+'.json')))
    geonames_salsah_data = None

    # reduce json grabbing by writing results to reusable files
    if not os.path.isfile(geonames_salsah_file):

        try:
            with urllib.request.urlopen('https://www.salsah.org/api/geonames/{}?reqtype=info'.format(id)) as url:

                geonames_salsah_data = json.loads(url.read().decode())

                with open(geonames_salsah_file, 'w') as json_file:
                    json.dump(geonames_salsah_data, json_file)
        
        except urllib.error.HTTPError:
            print('location not in salsah')
    else:
        with open(geonames_salsah_file) as f:
            geonames_salsah_data = json.load(f)

    if geonames_salsah_data:

        geonames_salsah = geonames_salsah_data['nodelist'].pop()
        
        geonames_id = geonames_salsah['name'].split(':')[1]

        geonames_file = '/'.join((geonames_dir, (str(geonames_id)+'.xml')))
        geonames_data = None

        # reduce json grabbing by writing results to reusable files
        if not os.path.isfile(geonames_file):
            response = requests.get('http://api.geonames.org/get?geonameId={}&username=thgie'.format(geonames_id))
            with open(geonames_file, 'wb') as file:
                file.write(response.content)

        parser = et.XMLParser(remove_blank_text=True)
        geonames_data = et.parse(geonames_file, parser)

        if geonames_data.findtext('name', default = 'None') == 'None':
            print(geonames_id)

        return geonames_data.getroot()
    
    else:

        return None

def clean_date(date_str):
    date_str = date_str.replace('GREGORIAN:', '')
    date_str = date_str.replace('CE:', '')
    date_str = date_str.replace(':', '/')

    return date_str

if __name__ == '__main__':
    main()
