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

windows = [2337, 2426, 2475, 2547, 2613, 2850, 2906, 2957, 2988]
dimensionsTested2 = [2]
dimensionsTested3 = [2]
weight = 100
epoches = [1, 501, 1001, 1501, 2001, 2501, 3001, 3501, 4001]


for epoch in epoches:
		for dimension2 in dimensionsTested2:
			for dimension3 in dimensionsTested3:
				arrayMSE = []
				activity1MSE = 0
				activity2MSE = 0
				activity3MSE = 0
				activity4MSE = 0
				activity5MSE = 0
				activity6MSE = 0
				activity7MSE = 0
				activity8MSE = 0
				maximum = 0
				minimum = 0
		

				string2 = "accell_x_imputed_test_weighted100" +"_d1_4n" + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+"_weightMult_" + str(weight)+".csv"

				for windowsIndex in range(8):
						print("reached" + str(dimension2) + str(dimension3) + " " + str(windowsIndex))

						imputedCSV = linecache.getline(string2, windows[windowsIndex])
						imputedCSV = stringToList(imputedCSV)
						imputedCSV = list(map(float, imputedCSV))
						dimension = len(imputedCSV)

						imputedCSV1 = linecache.getline(string2, windows[windowsIndex]+2)
						imputedCSV1 = stringToList(imputedCSV1)
						imputedCSV1 = list(map(float, imputedCSV1))
						arrayMSE = []

						trainOrder = []

						

						if(imputedCSV != imputedCSV1):

							refereceCSV = linecache.getline('accel_x_train_ref.csv', windows[windowsIndex])
							refereceCSV = stringToList(refereceCSV)
							refereceCSV = list(map(float, refereceCSV))

							trainOrder = linecache.getline('train_order.csv', windows[windowsIndex])
							trainOrder = stringToList(trainOrder)
							trainOrder = list(map(float, trainOrder))
	

							counter = 0
							for point in imputedCSV:
								temp = (refereceCSV[counter] - point) * (refereceCSV[counter] - point)
								arrayMSE.append(temp)
								counter = counter + 1

							maximum = max(arrayMSE)
							minimum = min(arrayMSE)

							plt = None
							
							import matplotlib.pyplot as plt
							df = None
							pltName = None
							pd = None
							import pandas as pd
							df=pd.DataFrame({'x_values': range(0,len(arrayMSE)), 'MSE': arrayMSE})
							plt.plot( 'x_values', 'MSE', data=df, marker='', markerfacecolor='blue',  linewidth=2)
							
							pltTitle = 'mse_accel_x'+' missing_30'+' activity_'+str(int(trainOrder[2]))+' d1=4n'+ ' d2='+ str(dimension2) + ' d3=' + str(dimension3) + ' epoches' + str(epoch)
							plt.title(pltTitle)
							plt.legend()
							plt.ylim(min(arrayMSE)*5, max(arrayMSE), )
							#pltName = 'accel_x_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
							#plt.set_title(pltName)
							pltName = pltTitle+'.png'
							plt.show()
							plt.savefig(pltName, bbox_inches='tight', dpi = 300)
							print("graph made: " + pltTitle)
							plt.clf()




						


				