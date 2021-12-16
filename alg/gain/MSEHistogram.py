import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import linecache

def stringToList(string):
    listRes = list(string.split(","))
    return listRes



def stringToList(string):
    listRes = list(string.split(","))
    return listRes

#windows = [2337, 2426, 2475, 2547, 2613, 2850, 2906, 2957, 2988]
windows = [2337, 2988]
dimensionsTested2 = [2]
dimensionsTested3 = [2]
weight = 100
epoches = [1, 501, 1001, 1501, 2001, 2501, 3001, 3501, 4001]
activity1 = []
activity2 = []
activity3 = []
activity4 = []
activity5 = []
activity6 = []
activity7 = []
activity8 = []
whole = []


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

				activity1 = []
				activity2 = []
				activity3 = []
				activity4 = []
				activity5 = []
				activity6 = []
				activity7 = []
				activity8 = []
				whole = []

		

				string2 = "accell_x_imputed_test_weighted100" +"_d1_4n" + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+"_weightMult_" + str(weight)+".csv"

				for windowsIndex in range(windows[0], windows[1]):
					print("reached" + str(dimension2) + str(dimension3) + " " + str(windowsIndex))

					imputedCSV = linecache.getline(string2, windowsIndex)
					imputedCSV = stringToList(imputedCSV)
					imputedCSV = list(map(float, imputedCSV))
					dimension = len(imputedCSV)

					imputedCSV1 = linecache.getline(string2, windowsIndex+2)
					imputedCSV1 = stringToList(imputedCSV1)
					imputedCSV1 = list(map(float, imputedCSV1))
					arrayMSE = []

					trainOrder = []

					

					if(imputedCSV != imputedCSV1):

						refereceCSV = linecache.getline('accel_x_train_ref.csv', windowsIndex)
						refereceCSV = stringToList(refereceCSV)
						refereceCSV = list(map(float, refereceCSV))

						trainOrder = linecache.getline('train_order.csv', windowsIndex)
						trainOrder = stringToList(trainOrder)
						trainOrder = list(map(float, trainOrder))


						counter = 0
						for point in imputedCSV:
							temp = (refereceCSV[counter] - point) * (refereceCSV[counter] - point)
							if trainOrder[2] == 1:
								activity1.append(temp)
							if trainOrder[2] == 2:
								activity2.append(temp)
							if trainOrder[2] == 3:
								activity3.append(temp)
							if trainOrder[2] == 4:
								activity4.append(temp)
							if trainOrder[2] == 5:
								activity5.append(temp)
							if trainOrder[2] == 6:
								activity6.append(temp)
							if trainOrder[2] == 7:
								activity7.append(temp)
							if trainOrder[2] == 8:
								activity8.append(temp)
							arrayMSE.append(temp)
							counter = counter + 1

						maximum = max(arrayMSE)
						minimum = min(arrayMSE)

				plt = None
				
				binWidth = 1
				import matplotlib.pyplot as plt
				plt.title("activity8 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity8)), int(max(activity8)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()
				plt = None

				import matplotlib.pyplot as plt
				plt.title("activity7 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity7)), int(max(activity7)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()
				plt = None

				import matplotlib.pyplot as plt
				plt.title("activity6 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity6)), int(max(activity6)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()
				plt = None


				import matplotlib.pyplot as plt
				plt.title("activity5 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity5)), int(max(activity5)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()

				plt = None

				import matplotlib.pyplot as plt
				plt.title("activity4 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity4)), int(max(activity4)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()
				plt = None


				import matplotlib.pyplot as plt
				plt.title("activity3 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity3)), int(max(activity3)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()
				plt = None


				import matplotlib.pyplot as plt
				plt.title("activity2 " + str(epoch))
				plt.hist(activity8, bins=range(int(min(activity2)), int(max(activity2)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				plt.show()
				plt = None

				# import matplotlib.pyplot as plt
				# plt.title("activity1 " + str(epoch))
				# plt.hist(activity8, bins=range(int(min(activity1)), int(max(activity1)) + binWidth, binWidth), edgecolor="yellow", color = "brown")
				# plt.show()
				# plt = None


							# df = None
							# pltName = None
							# pd = None
							# import pandas as pd
							# df=pd.DataFrame({'x_values': range(0,len(arrayMSE)), 'MSE': arrayMSE})
							# plt.plot( 'x_values', 'MSE', data=df, marker='', markerfacecolor='blue',  linewidth=2)
							
							# pltTitle = 'mse_accel_x'+' missing_30'+' activity_'+str(int(trainOrder[2]))+' d1=4n'+ ' d2='+ str(dimension2) + ' d3=' + str(dimension3) + ' epoches' + str(epoch)
							# plt.title(pltTitle)
							# plt.legend()
							# plt.ylim(min(arrayMSE)*5, max(arrayMSE), )
							# #pltName = 'accel_x_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
							# #plt.set_title(pltName)
							# pltName = pltTitle+'.png'
							# plt.show()
							# plt.savefig(pltName, bbox_inches='tight', dpi = 300)
							# print("graph made: " + pltTitle)
							# plt.clf()




						


				