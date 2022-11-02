'''

    

'''
import argparse, csv, json, os, re, requests, sys, time, urllib

csv.field_size_limit(sys.maxsize)

def main():

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    with open (filename) as f:
        datareader = csv.reader(f, delimiter=';', quotechar='"')
        row_count = 0

        for row in datareader:
            row_count += 1
            if row_count % 25 == 0:
                print('Checked '+str(row_count)+' lines.')
            
            if(row[0] != 'schema:identifier'):
                ids = row[0].split('|')

                if(len(ids) > 1):
                    insert_old_nr(ids)
                    

def insert_old_nr(ids):
    with urllib.request.urlopen("https://participatory-archives.ch/api/items?property[0][property]=1632&property[0][type]=eq&property[0][text]="+ids[0]) as url:
        data = json.load(url)[0]

        if(len(data['schema:identifier']) == 1):

            headers = requests.structures.CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Content-Type"] = "application/json"

            url = 'https://participatory-archives.ch/api/items/'+str(data['o:id'])+'?key_identity=7oxjvW9SHAwDSDd3nzFjoe94nC29LBeI&key_credential=ePBflYKBPowsHLaUkNn767jAjZAQBpn0'
            
            data['schema:identifier'].append({
                        'type': 'literal',
                        'property_id': 1632,
                        '@value': ids[1]
                    })

            r = requests.patch(url, data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    main()
