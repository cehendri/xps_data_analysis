#imports required pre-processing toolkit
import pandas as pd
from sklearn import preprocessing
	
#normalize data between 0 and 1
def normalize_data(spectra):	
	#rename columns from spectra
	spectra.columns = ['BE1','BE2','Int1','BE3','BE4','Int2']
	#define the type of pre-processing to be between 0 and 1
	min_max = preprocessing.MinMaxScaler()
	#takes the data and applies transform to the abundance columns
	norm = min_max.fit_transform(spectra[['Int1','Int2']])
	#converts the result to a DataFrame
	norm_data = pd.DataFrame(norm)
	return norm_data
	
	