'''


    

'''
import argparse, csv, json, os, re, requests, sys, time, urllib

import mysql.connector

def main():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="omeka"
    )

    cursor = mydb.cursor()

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    with open (filename) as f:
        datareader = csv.reader(f, delimiter=';', quotechar='"')
        row_count = 0
        old_nr_count = 0

        for row in datareader:
            row_count += 1
            
            if(row[0] != 'schema:identifier'):
                ids = row[0].split('|')

                if(len(ids) > 1):

                    old_nr_count += 1

                    cursor.execute("SELECT * FROM `value` WHERE `value` = '"+ids[0]+"'")
                    result = cursor.fetchall()

                    cursor.execute("SELECT * FROM `value` WHERE `property_id` = 1632 and `resource_id` = "+str(result[0][1]))
                    result = cursor.fetchall()

                    if(len(result) == 1):
                        cursor.execute("INSERT INTO `value` (`resource_id`, `property_id`, `value_resource_id`, `value_annotation_id`, `type`, `lang`, `value`, `uri`, `is_public`) VALUES ("+str(result[0][1])+", 1632, NULL, NULL, 'literal', NULL, '"+ids[1]+"', NULL, 1)")
        
        print(old_nr_count)
        mydb.commit()
                    

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
