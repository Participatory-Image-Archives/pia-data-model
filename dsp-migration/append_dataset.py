import argparse, csv, re

def main():

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

    # fix newlines in cells before starting to work on it
    with open (filename, 'r' ) as f:
        content = f.read()
        csv_string = re.sub(r'([^;])\n', r'\1\\n', content, flags = re.M)
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

    # parse file into proper data structure
    datareader = csv.reader(csv_lines)

    for row in datareader:

        current_index += 1

        data_row = row[0].split(';')

        if(data_row[0] != ''):

            # reset object
            if current_index > 0:
                data.append(current_parent)
                current_parent = []

        current_parent.append(data_row)

    for obj in data:

        if obj[0][1] == ':Object':

            # check if object needs to have dataset relation attached
            dataset = ''
            signature_parts = obj[0][2].split('_')

            collection = signature_parts[1]
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

    # construct csv string to write out
    csv_out = ''

    for obj in data:
        for line in obj:
            csv_out = csv_out + ';'.join(line) + '\n'

    new_filename = filename.rsplit('.', 1)[0]+'_ds.csv'

    text_file = open(new_filename, 'w')
    text_file.write(csv_out)
    text_file.close()

if __name__ == '__main__':
    main()
