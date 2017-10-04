# The project imports XPS data and performs analysis and fitting for peaks

## XPS data was collected using  a PHI5400 XPS by Christophper Hendricks and Azzam Mansour

*The data has been pre-processed so that binding energies are shifted so that the LiF peak is located at 685 eV
*Column 2 is the 0 Volt battery shifted binding energy
*Column 3 is the 0 Volt battery counts/sec from the hemispherical electron detector
*Column 5 is the 3.4 Volt battery shifted binding energy
*Column 6 is the 3.4 Volt battery counts/sec from the hemispherical electron detector

##xps_data_extractor
Utility to read experimental XPS output
Input:
* dir_path: path to folder with experimental data
* xps_input_mask: experimental data output mask, default = 'Multiplex Data'
* xps_input_format: name of input data format, default ='xlsx'
* elements: list of elements to look data for, dafault = ['O', 'F', 'C']

Output: 
data structure{
  element_1: {
    experiment_1: [binding_energies, abandance],
    experiment_2: [binding_energies, abandance],
    ...
  },
  element_2: {
    experiment_1: [binding_energies, abandance],
    experiment_2: [binding_energies, abandance],
    ...
  }
  ...
}

from xps_data_extractor import XPSImporter
xps_importer = XPSImporter()
result = xps_importer.load()
