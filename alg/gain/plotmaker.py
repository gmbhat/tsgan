import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import linecache

def stringToList(string):
    listRes = list(string.split(","))
    return listRes

#lineNumber = 2613
# lineNumber = 2906

# imputedCSV = linecache.getline('accel_z_imputed_train.csv',lineNumber)
# imputedCSV = stringToList(imputedCSV)
# imputedCSV = list(map(float, imputedCSV))
# print("-------------------------------------------------------- length of imputed = " +str(len(imputedCSV)))

# refereceCSV = linecache.getline('accel_z_train_ref.csv',lineNumber)
# refereceCSV = stringToList(refereceCSV)
# refereceCSV = list(map(float, refereceCSV))

# missngCSV = linecache.getline('accel_z_train.csv',lineNumber) #csv.reader('stretch_missing_train.csv')
# missngCSV = stringToList(missngCSV)
# missngCSV = list(map(float, missngCSV))


# df=pd.DataFrame({'x_values': range(1,184), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
 
# # multiple line plots
# plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
# plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
# plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
# # show legend
# plt.legend()



# # show graph
# plt.show()

def stringToList(string):
    listRes = list(string.split(","))
    return listRes

epoches = [3000]
windows = [2494]
dimensionsTested1 = [18]
dimensionsTested2 = [12]
dimensionsTested3 = [18]


for epoch in epoches:
	for dimension1 in dimensionsTested1:
		for dimension2 in dimensionsTested2:
			for dimension3 in dimensionsTested3:
				string2 = "Mass run small architectures\\accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"

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

					imputedCSV = linecache.getline(string2, plotWindow)
					imputedCSV = stringToList(imputedCSV)
					imputedCSV = list(map(float, imputedCSV))

					refereceCSV = linecache.getline('accel_x_train_ref.csv',plotWindow)
					refereceCSV = stringToList(refereceCSV)
					refereceCSV = list(map(float, refereceCSV))

					missngCSV = linecache.getline('accel_x_train.csv',plotWindow) #csv.reader('stretch_missing_train.csv')
					missngCSV = stringToList(missngCSV)
					missngCSV = list(map(float, missngCSV))

					train_order_csv = linecache.getline('train_order.csv', plotWindow)
					train_order_csv = stringToList(train_order_csv)
					train_order_csv = list(map(float, train_order_csv))
					activity = train_order_csv[2]
					missing_data_percent = train_order_csv[1]




					df=pd.DataFrame({'x_values': range(1,184), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
					plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
					plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
					plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
					pltTitle = 'accel_x'+' missing_'+str(int(missing_data_percent*100))+' activity_'+str(int(activity))+' d1=' + str(dimension1) + ' d2='+ str(dimension2) + ' d3=' + str(dimension3) + ' window=' + str(plotWindow) + ' epoches' + str(epoch)
					plt.title(pltTitle)
					plt.legend()
					#pltName = 'accel_x_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
					#plt.set_title(pltName)
					pltName = pltTitle+'.png'
					plt.savefig(pltName, bbox_inches='tight', dpi = 300)

					plt.clf()
