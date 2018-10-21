'''
    This script helps in detecting whether there were any discrepencies in the labelling of images using LabelImg.
    It basically accepts CSV input, and prints the names of those files, where bounding boxes were marked in such a way,
    that one or more of their edges are not inside the image being labelled.
    This script would help us in catching errors which would otherwise cause model training to fail whenever such an image is encountered.
    Usage:
        Kindly search for "TODO" tags in the file and make changes to them as mentioned with each TODO.
        Run the file with the following command from the root folder of the repo:
            python3 utils/detect_incorrectly_labelled_data.py
'''

import csv

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    incorrect_labels=[]
    incorrect_file_names=[]
    correct=[]

    for line in reader:
        width = line["width"]
        height = line["height"]

        xmin = int(line["xmin"])
        xmax = int(line["xmax"])
        ymin = int(line["ymin"])
        ymax = int(line["ymax"])

        range_for_x = range(0, int(width)+1)
        range_for_y = range(0, int(height)+1)

        if xmin in range_for_x:
            correct.append(line)
        else:
            incorrect_labels.append(line)
            incorrect_file_names.append(line["filename"])

        if xmax in range_for_x:
            correct.append(line)
        else:
            incorrect_labels.append(line)
            incorrect_file_names.append(line["filename"])

        if ymin in range_for_y:
            correct.append(line)
        else:
            incorrect_labels.append(line)
            incorrect_file_names.append(line["filename"])

        if ymax in range_for_y:
            correct.append(line)
        else:
            incorrect_labels.append(line)
            incorrect_file_names.append(line["filename"])

    print(set(incorrect_file_names))




if __name__ == "__main__":
    # TODO: Change PATH_TO_CSV_FILE to the path where the faulty CSV file is stored
    with open("PATH_TO_CSV_FILE") as f_obj:
        csv_dict_reader(f_obj)
