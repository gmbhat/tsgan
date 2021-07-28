import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import linecache

def stringToList(string):
    listRes = list(string.split(","))
    return listRes

lineNumber = 2850

imputedCSV = linecache.getline('stretch_imputed_train_d3_8.csv',lineNumber)
imputedCSV = stringToList(imputedCSV)
imputedCSV = list(map(float, imputedCSV))

refereceCSV = linecache.getline('stretch_ref_train.csv',lineNumber)
refereceCSV = stringToList(refereceCSV)
refereceCSV = list(map(float, refereceCSV))

missngCSV = linecache.getline('stretch_missing_train.csv',lineNumber) #csv.reader('stretch_missing_train.csv')
missngCSV = stringToList(missngCSV)
missngCSV = list(map(float, missngCSV))


df=pd.DataFrame({'x_values': range(1,72), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
 
# multiple line plots
plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
# show legend
plt.legend()

# show graph
plt.show()