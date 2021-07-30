import os
#import pandas as pd
import csv
#import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt 
#import pyplot as plt
import numpy as np
#import pandas as pd
import csv
import linecache


def stringToList(string):
    listRes = list(string.split(","))
    return listRes

windows = [228, 463, 822, 1057, 1416, 1651, 2010, 2245, 2613, 2850]
dimensionsTested = [1, 2, 4, 8]


file_to_rename = "stretch_imputed_train.csv"


for dimension in dimensionsTested:
    print("-------------------------------------- stretch_test third layer d/"+str(dimension)+" --------------------------------")
    string1 = "python gain.py -i stretch_missing_train.csv -o stretch_imputed_train.csv --T 1 --f 1 --s 1 --t " + str(dimension) + " --testfile stretch_missing_test.csv"
    os.system(string1)
    string2 = "stretch_imputed_train_d3_"+str(dimension)+".csv"
    os.rename(file_to_rename, string2)
    print("-------------------------------------- stretch_test third layer d/"+str(dimension)+" --------------------------------")
    for plotWindow in windows:
        plt = None
        imputedCSV = None
        refereceCSV = None
        missngCSV = None
        train_order_csv = None
        activity = None
        missing_data_percent = None
        import matplotlib.pyplot as plt
        df = None
        pltName = None
        pd = None
        import pandas as pd

        imputedCSV = linecache.getline('stretch_imputed_train_d3_'+str(dimension)+'.csv',plotWindow)
        imputedCSV = stringToList(imputedCSV)
        imputedCSV = list(map(float, imputedCSV))

        refereceCSV = linecache.getline('stretch_ref_train.csv',plotWindow)
        refereceCSV = stringToList(refereceCSV)
        refereceCSV = list(map(float, refereceCSV))

        missngCSV = linecache.getline('stretch_missing_train.csv',plotWindow) #csv.reader('stretch_missing_train.csv')
        missngCSV = stringToList(missngCSV)
        missngCSV = list(map(float, missngCSV))

        train_order_csv = linecache.getline('train_order.csv', plotWindow)
        train_order_csv = stringToList(train_order_csv)
        train_order_csv = list(map(float, train_order_csv))
        activity = train_order_csv[2]
        missing_data_percent = train_order_csv[1]