# Object-Detection-Pipeline
Pipeline for training a Tensorflow Object Detection model

## Setting Up

### Install Python3

#### On Mac
`brew install python3`

#### On Linux machines
```
sudo apt-get update
sudo apt-get install python3.6
```

### Set up a virtual environment
Virtual environments are created in order to isolate Python dependencies for different projects that we may be working on.

#### Install virtualenv
`pip3 install virtualenv`

#### Create a virtual environment for this project
`python3 -m virtualenv object-detection`

### Install dependencies
Run the following command from the root directory of the repository to install dependencies:<br/>
`pip3 install -r requirements.txt`

### Setup protobuf compiler (Google's compiler used in TensorFlow):

#### On Mac
`brew install protobuf`

#### On Linux
`https://gist.github.com/sofyanhadia/37787e5ed098c97919b8c593f0ec44d8`

### Add libraries to PYTHONPATH
When running locally, the project's directory and slim directories should be appended to PYTHONPATH. This can be done by running the following from root of the repo:

``` bash
# From root of the repository
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

Note: This command needs to run from every new terminal you start. If you wish to avoid running this manually, you can add it as a new line to the end of your ~/.bashrc file, replacing `pwd` with the absolute path of the repository folder on your system.

### Test the setup
Run this to verify whether Tensorflow object detection has been setup properly or not:<br/>
`python3 object_detection/builders/model_builder_test.py`


### Setup directory structure required for easy file handling
Run this from the root folder of the repository<br/>
`python3 setup.py `
