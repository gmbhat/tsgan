import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import linecache

print("hello")

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
refereceCSV = []
vals = []


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
				vals = []

		

				string2 = "accell_x_imputed_test_weighted100" +"_d1_4n" + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+"_weightMult_" + str(weight)+".csv"

				for windowsIndex in range(windows[0], windows[1]):
					#print("reached" + str(dimension2) + str(dimension3) + " " + str(windowsIndex))

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
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 2:
								activity2.append(temp)
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 3:
								activity3.append(temp)
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 4:
								activity4.append(temp)
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 5:
								activity5.append(temp)
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 6:
								activity6.append(temp)
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 7:
								activity7.append(temp)
								vals.append(refereceCSV[counter])
							if trainOrder[2] == 8:
								activity8.append(temp)
								vals.append(refereceCSV[counter])
							arrayMSE.append(temp)
							
							counter = counter + 1
							

						maximum = max(arrayMSE)
						minimum = min(arrayMSE)

				plt = None
				print(len(vals))
				print(len(activity8))
				import matplotlib.pyplot as plt
				#print(activity8)
				plt.title("activity8 " + str(epoch))
				plt.scatter(activity8, vals, marker = None, s = 10)
				plt.show()