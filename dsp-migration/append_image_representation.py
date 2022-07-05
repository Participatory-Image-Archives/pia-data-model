import argparse, csv, re

def main():

    # setup script
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-F', '--file', help='csv file')
    args = arg_parser.parse_args()

    filename = args.file

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

    for obj in data:

        obj_count += 1
        print('Worked through '+str(obj_count)+' of '+str(len(data))+' objects.')

        if obj[0][1] == ':Object':

            # create propery that needs to be appended
            prop = []

            for i in range(6):
                prop.append('')

            # check if image or moving image representation
            type = 'Image'
            filetype = obj[0][5]

            if filetype == '':
                continue

            filetype = obj[0][5].rsplit('.', 1)[1]

            if 'mp4' in filetype:
                type = 'MovingImage'

            # hasImageRepresentation;text-prop;;SGV_09P_05312-rep;utf8;;prop-default

            prop.append('has'+type+'Representation')
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
            image_representation.append(':'+type+'Representation')
            image_representation.append(obj[0][2])
            image_representation.append('')
            image_representation.append('res-default')
            image_representation.append(obj[0][5])

            for i in range(213):
                image_representation.append('')

            image_representations.append([image_representation])

    data = data + image_representations

    print('Writing appended CSV file.')

    csv_data = []

    for obj in data:
        for line in obj:
            csv_data.append(line)


    new_filename = filename.rsplit('.', 1)[0]+'_ir.csv'

    with open(new_filename, 'w+') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(csv_data)


if __name__ == '__main__':
    main()
