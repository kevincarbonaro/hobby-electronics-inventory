# Class for taking care of anything related to reading and writing to disk.
import json

class Storage:

    def __init__(self, path_data_structure):
        self.dataStructure = ""
        self.pathDataStructure = path_data_structure

    # Read data structure
    def ReadDataStructure(self):
        fileDataStructure = open(self.pathDataStructure)
        self.dataStructure = fileDataStructure.read()
    #
