'''

    This script creates a delta between the places already
    in omeka and the new ones. Bulk Import can't handle
    csv imports where there are existing and new entries
    together in one list.

'''
import argparse, csv, json, os, re, requests, sys, urllib

csv.field_size_limit(sys.maxsize)

def main():

    # secondary objects
    new_places = []         # schema:location
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

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    with open (filename) as f:
        datareader = csv.reader(f, delimiter=';', quotechar='"')
        row_count = 0
        new_count = 0

        for row in datareader:
            row_count += 1
            if row_count % 25 == 0:
                print('Checked '+str(row_count)+' lines.')
            
            if(row[0] != 'schema:identifier'):
                with urllib.request.urlopen("https://pia-omeka.test/api/items?property[0][property]=1632&property[0][type]=eq&property[0][text]="+row[0]) as url:
                    data = json.load(url)
                    if(len(data) == 0):
                        new_places.append({
                            'schema:identifier': row[0],
                            'schema:name': row[1],
                            'schema:geo ^^geometry:geography:coordinates': row[6],
                            'schema:elevation': row[4],
                            'pia:population': row[5],
                            'pia:geometry ^^geometry': row[7],
                            'schema:url ^^uri': row[8]
                        })
                        new_count += 1
                        print(str(new_count)+' new places.')
                    else:
                        print('.')

    with open('new_places.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = places_header, delimiter=';')
        writer.writeheader()
        writer.writerows(new_places)
            

if __name__ == '__main__':
    main()
