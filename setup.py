import os

parent_directory_names = ["input_images", "csv_data_and_classes", "labelled_xml_data", "tfrecords", "model_training", "trained_model"]
subdirectory_names = ["train", "test"]

for directory_name in parent_directory_names:
    cwd = os.getcwd()

    directory_to_be_created = os.path.join(cwd, directory_name)

    # Create parent if it is not present
    if not os.path.exists(directory_to_be_created):
        print("Creating directory {}".format(directory_to_be_created))
        os.mkdir(directory_to_be_created)
        print("Created successfully!")
    else:
        print("Directory {} already exists".format(directory_to_be_created))

    # Create subdirectories
    if directory_name == "input_images" or directory_name == "labelled_xml_data":
        for subdirectory_name in subdirectory_names:
            subdirectory_to_be_created = os.path.join(directory_to_be_created, subdirectory_name)

            if not os.path.exists(subdirectory_to_be_created):
                print("Creating subdirectory {}".format(subdirectory_to_be_created))
                os.mkdir(subdirectory_to_be_created)
                print("Created successfully!")
            else:
                print("Subdirectory {} already exists".format(subdirectory_to_be_created))
