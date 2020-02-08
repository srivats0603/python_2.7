import pandas as pd
import numpy as np
from pandas import DataFrame as df
import os

base_out_folder = r'C:\Users\ADMIN\Documents\PythonScripts\generalexamples\readCSV_produce_text\output'
base_in_folder = r'C:\Users\ADMIN\Documents\PythonScripts\generalexamples\readCSV_produce_text'

farm_names = ['Vanxx']

for thisFarm in farm_names:
    start_index = 0
    last_timestamp = 20190731
    end_index = start_index+23
    
    infilename = thisFarm+'.csv'
    infilename = os.path.join(base_in_folder,infilename)
    forecastDf = pd.read_csv(infilename)
    forecastDf['forecast_2shift'] = forecastDf['forecast_2shift'].round(0)

    while(end_index<=len(forecastDf)):
        forecastSubDf = forecastDf.loc[start_index:end_index]
        filename = str(last_timestamp) + '_XXX2_'+thisFarm+'.txt'
        filename =  os.path.join(base_out_folder,filename)
        np.savetxt(filename, forecastSubDf.values, fmt='%d')

        last_timestamp = str(forecastSubDf.loc[end_index,'time'])[0:8]

        print last_timestamp
        start_index = end_index+1
        end_index = start_index+23
    

