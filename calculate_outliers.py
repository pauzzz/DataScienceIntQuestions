import pandas as pd
import numpy as np

def outlierRow(column):
	#calculate the IQR
    df=pd.DataFrame(column)
    range=df.quantile([0.25,0.75])
    IQR=range.iloc[1]-range.iloc[0]
    maxData=range.iloc[1]+1.5*IQR
    minData=range.iloc[0]-1.5*IQR
    outliers=[]
    for i in column:
        if i>maxData[0]:
            print('Row identified as upper outlier: ' +str(i))
            outliers.append(i)

        elif i<minData[0]:
            print('Row identified as lower outlier: ' +str(i))
            outliers.append(i)

    return outliers

column=[6,1,2,3,1,5,2,2,5,2,3,1,2,45,5,1,53,1,-50, -24,0,2,4,6,1,2,7,2,7,1]

outlierRow(column)

