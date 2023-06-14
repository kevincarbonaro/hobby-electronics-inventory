# This class is used to create an object enabling reading
# and saving data to/from flat files
class Storage

<<<<<<< HEAD
import json


class Storage:

    def __init__(self, path_data_structure):
        self.dataStructure = ""
        self.pathDataStructure = path_data_structure

    # Read data structure
    def ReadDataStructure(self):
        fileDataStructure = open(self.pathDataStructure)
        self.dataStructure = fileDataStructure.read()
=======
    #
>>>>>>> parent of e7d0c98... Storage Class
