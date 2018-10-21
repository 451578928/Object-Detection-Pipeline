'''
    This file takes the XML output generated using LabelImg, and converts it to CSV.
    By default, it takes training data from labelled_xml_data/train and testing data from labelled_xml_data/test.
    It outputs the test and train CSV files generated to csv_data_and_classes/test.csv and labelled_xml_data/train.csv respectively.
    How to run (from root directory of the project):
        python3 xml_to_csv.py
'''

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

# Handles nested folders
def generate_csv_data(dir_path, output_path):
    sub_directories = [s.rstrip("/") for s in glob.glob(dir_path + "*/")]
    print(sub_directories)

    for sub_directory in sub_directories:
        if sub_directory == dir_path:
            continue
        generate_csv_data(sub_directory, output_path)

    xml_df = xml_to_csv(dir_path)
    xml_df.to_csv(output_path, index=None, mode='a')

def main():
    # TODO: Change the second parameter in the line below as per your needs.
    # This denotes which folder the XML files are to be picked up from.
    train_folder_path = os.path.join(os.getcwd(), 'labelled_xml_data/train/')
    test_folder_path = os.path.join(os.getcwd(), 'labelled_xml_data/test/')

    output_train_folder_path = os.path.join(os.getcwd(), 'csv_data_and_classes/train.csv')
    output_test_folder_path = os.path.join(os.getcwd(), 'csv_data_and_classes/test.csv')


    generate_csv_data(train_folder_path, output_train_folder_path)
    generate_csv_data(test_folder_path, output_test_folder_path)

    print('Successfully converted xml to csv.')


main()
