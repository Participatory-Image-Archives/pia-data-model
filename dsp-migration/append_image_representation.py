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
    image_representations = []

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

            # create propery that needs to be appended
            prop = []

            for i in range(6):
                prop.append('')

            # hasImageRepresentation;text-prop;;SGV_09P_05312-rep;utf8;;prop-default

            prop.append('hasImageRepresentation')
            prop.append('text-prop')
            prop.append('')
            prop.append(obj[0][2]+'-rep')
            prop.append('utf8')
            prop.append('')
            prop.append('prop-default')

            for i in range(206):
                prop.append('')

            obj.append(prop)

            # create new image representation object
            # SGV_09P_05312-rep;:ImageRepresentation;SGV_09P_05312;;res-default;sgv.dir/images/SGV_09P_05312.TIF
            image_representation = []

            image_representation.append(obj[0][2]+'-rep')
            image_representation.append(':ImageRepresentation')
            image_representation.append(obj[0][2])
            image_representation.append('')
            image_representation.append('res-default')
            image_representation.append('sgv.dir/images/'+obj[0][2]+'.TIF')

            for i in range(213):
                image_representation.append('')

            image_representations.append([image_representation])

    data = data + image_representations

    # construct csv string to write out
    csv_out = ''

    for obj in data:
        for line in obj:
            csv_out = csv_out + ';'.join(line) + '\n'

    new_filename = filename.rsplit('.', 1)[0]+'_appended.csv'

    text_file = open(new_filename, 'w')
    text_file.write(csv_out)
    text_file.close()
        


if __name__ == '__main__':
    main()
