import pandas as pd
import numpy as np
from pandas import DataFrame as df
from datetime import datetime

def findAutoCorrelation(df_y):
    df_y = df_y-np.mean(df_y)
    sumSquare = np.sum(df_y**2)
    corrCoeff = np.correlate(df_y,df_y)*100/sumSquare
    
    return corrCoeff


if __name__ == '__main__':
    df = pd.DataFrame({'B': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    df['Bshift'] = df['B'].shift(2)
    df = df.dropna(axis=0,how='any')
    print df
    print df.diff()
    print findAutoCorrelation(df['B'])
    sumSquare = np.sum(df['B']**2)
    corrArr = np.correlate(df['B'], df['Bshift'],mode='full')*100/sumSquare
    print len(corrArr)
