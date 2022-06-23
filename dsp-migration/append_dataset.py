import argparse, csv, re

def main():

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    print('Fixing linebreaks in CSV file.')

    # fix newlines in cells before starting to work on it
    with open (filename, 'r' ) as f:
        content = f.read()
        csv_string = re.sub(r'([^;];)[\n]+', r'\1\\n', content, flags = re.M)
        csv_string = re.sub(r'([^;])\n', r'\1\\n', csv_string, flags = re.M)
        csv_lines = csv_string.splitlines()

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

    print('Opening CSV file for reading.')

    # parse file into proper data structure
    datareader = csv.reader(csv_lines)

    print('Parsing CSV file into data structure.')

    for row in datareader:

        if current_index % 100000 == 0:
            print('Parsed '+str(current_index)+' lines.')
        current_index += 1

        data_row = row[0].split(';')

        if(data_row[0] != ''):

            # reset object
            if current_index > 0:
                data.append(current_parent)
                current_parent = []

        current_parent.append(data_row)

    obj_count = 1

    for obj in data:

        obj_count += 1
        print('Worked through '+str(obj_count)+' of '+str(len(data))+' objects.')

        if obj[0][1] == ':Object':

            # check if object needs to have dataset relation attached
            dataset = ''
            signature_parts = obj[0][2].split('_')

            if len(signature_parts) < 3:
                continue

            collection = signature_parts[1]

            if collection != '17D' and collection != '17N':
                continue

            object_id = int(signature_parts[2])

            if collection == '17D':
                if object_id >= 1 and object_id <= 372:
                    dataset = 'dataset_a'

                if object_id >= 373 and object_id <= 379:
                    dataset = 'dataset_b'
            
            if signature_parts[1] == '17N':
                if object_id >= 1 and object_id <= 840:
                    dataset = 'dataset_a'

                if object_id >= 841 and object_id <= 1248:
                    dataset = 'dataset_b'

            if dataset == '':
                continue

            # create propery that needs to be appended
            prop = []

            for i in range(6):
                prop.append('')

            # hasDataset;resptr-prop;;sgv_17_set_a;;;prop-default
            prop.append('hasDataset')
            prop.append('resptr-prop')
            prop.append('')
            prop.append(dataset)
            prop.append('')
            prop.append('')
            prop.append('prop-default')

            for i in range(206):
                prop.append('')

            obj.append(prop)

    # create new dataset objects
    # sgv_17_set_a;:Dataset;sgv_17_set_a;;res-default
    dataset_a = []
    dataset_b = []

    dataset_a.append('sgv_17_set_a')
    dataset_a.append(':Dataset')
    dataset_a.append('sgv_17_set_a')
    dataset_a.append('')
    dataset_a.append('res-default')

    dataset_b.append('sgv_17_set_b')
    dataset_b.append(':Dataset')
    dataset_b.append('sgv_17_set_b')
    dataset_b.append('')
    dataset_b.append('res-default')

    for i in range(214):
        dataset_a.append('')
        dataset_b.append('')

    data = data + [[dataset_a]]
    data = data + [[dataset_b]]

    print('Writing appended CSV file.')

    csv_data = []

    for obj in data:
        for line in obj:
            csv_data.append(line)

    new_filename = filename.rsplit('.', 1)[0]+'_ds.csv'

    with open(new_filename, 'w+') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(csv_data)

if __name__ == '__main__':
    main()
