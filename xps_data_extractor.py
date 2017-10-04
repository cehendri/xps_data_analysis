import pandas as pd
import glob, os
import numpy as np

#input: file directory, xps data filemask and format, list of elements
#output:

class XPSImporter:

    def __init__(self, dir_path, xps_input_mask='Multiplex Data', xps_input_format='xlsx', elements=['C']):
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

                    if 'xls' in self.xps_input_format:
                        data = pd.read_excel(self.dir_path + '/' + file)
                    if 'csv' in self.xps_input_format:
                        data = pd.read_csv(self.dir_path + '/' + file)

                    columns_count = len([name for name in data.keys() if 'unnamed' not in name.lower()])
                    columns = data.keys()

                    for column in range(columns_count):
                        init_column_id = round(column * len(columns) / columns_count)
                        column_id = round((column + 1) * len(columns) / columns_count) - 1
                        output_structure[element][columns[init_column_id]] = np.array(
                            [[d for d in data[columns[column_id - 1]]],
                             [d for d in data[columns[column_id]]]])

        return output_structure