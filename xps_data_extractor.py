import pandas as pd
import glob, os
import numpy as np

#input: file directory, xps data filemask and format, list of elements
#output:

class XPSImporter:

    def __init__(self, dir_path='/home/olga/Documents/ECSHackDay/XPSprojext/xps_data_analysis/', xps_input_mask='Multiplex Data', xps_input_format='xlsx', elements=['O', 'F', 'C']):
        #Initialize and set up pathway to folder, filename mask and format of the data

        self.dir_path = dir_path
        self.xps_input_mask = xps_input_mask
        self.xps_input_format = xps_input_format
        self.elements = elements

        self.output_structure = {}


    def load(self):
        os.chdir(self.dir_path)
        self.available_files = glob.glob("*." + self.xps_input_format)

        self.input_files = {}
        for element in self.elements:
            self.input_files[element] = []

# TODO: less hardcoded reading of filenames and extracting elements from filenames
        for file in glob.glob("*." + self.xps_input_format):
            if self.xps_input_mask in file:
                self.input_files[file[17]].append(file)
        print('Found files', self.input_files)

        output_structure = {}
        for element in self.elements:
            print('Extracting data for ', element)
            print('Found ', len(self.input_files[element]), 'files.')
            output_structure[element] = {}
            if len(self.input_files[element]) > 0:
                for file in self.input_files[element]:
                    print('\tReading ', file)
                    data = pd.read_excel(self.dir_path + '/' + file)
                    columns = data.keys()
#TODO: reading arbitrary amount of columns
                    output_structure[element][columns[0]] = np.array(
                        [[d for d in data[columns[1]]], [d for d in data[columns[2]]]])
                    output_structure[element][columns[3]] = np.array(
                        [[d for d in data[columns[4]]], [d for d in data[columns[5]]]])  # 5 and 6

        return output_structure
