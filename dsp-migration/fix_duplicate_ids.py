import argparse, csv, re

def main():

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    data = []

    '''
    data
        object
            mainline
            sublines
    '''

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

    obj_count = 1

    object_ids = []
    representation_ids = []

    for obj in data:

        if obj[0][1] == ':Object':
            for row in obj:
                if row[6] == 'hasImageRepresentation':
                    if row[9] in object_ids:
                        id_count = 1
                        while row[9]+'-'+str(id_count) in object_ids:
                            id_count += 1
                        object_ids.append(row[9]+'-'+str(id_count))
                        row[9] = row[9]+'-'+str(id_count)
                    else:
                        object_ids.append(row[9])
  
        if obj[0][1] == ':ImageRepresentation':
            if obj[0][0] in representation_ids:
                id_count = 1
                while obj[0][0]+'-'+str(id_count) in representation_ids:
                    id_count += 1
                representation_ids.append(obj[0][0]+'-'+str(id_count))
                obj[0][0] = obj[0][0]+'-'+str(id_count)
            else:
                representation_ids.append(obj[0][0])
  
    print('Writing fixed CSV file.')

    csv_data = []

    for obj in data:
        for line in obj:
            csv_data.append(line)

    new_filename = filename.rsplit('.', 1)[0]+'_fixed_ids.csv'

    with open(new_filename, 'w+') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(csv_data)

if __name__ == '__main__':
    main()
