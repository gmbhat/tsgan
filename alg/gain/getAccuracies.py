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
import math
import statistics
from sklearn.metrics import mean_squared_error




epoches = [2000, 3000, 4000, 5000, 6000, 8000, 10000]
dimensionsTested1 = [8, 10, 12, 16, 18, 20]
dimensionsTested2 = [8, 10, 12, 16, 18, 20]
dimensionsTested3 = [8, 10, 12, 16, 18, 20]
windows = [2377, 2426, 2475, 2547, 2613, 2850, 2906, 2957, 2989]

def stringToList(string):
    listRes = list(string.split(","))
    return listRes

def multiplyList(list, meanToHundred):
	result = 1
	index = 0
	listReturning = []
	for current in list:
		result = current * meanToHundred
		listReturning.insert(index, result)
		index = index + 1
	return listReturning

# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])


# with open('accel_x_accuracy.csv', 'w') as csvfile:
# 	filewriter = csv.writer(csvfile)
# 	filewriter.writerow(["Epochs", "d1", "d2", "d3", "missing percent", "Activity", "Average MSE", "Average percent difference", "Memory in KB", "best window", "best percent"])




	# for epoch in epoches:
	# 	for dimension1 in dimensionsTested1:
	# 		for dimension2 in dimensionsTested2:
	# 			for dimension3 in dimensionsTested3:
	# 				string2 = "accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"
					
	# 				for window in windows:
	# 					imputedCSV = linecache.getline(string2, window)
	# 					imputedCSV = stringToList(imputedCSV)
	# 					imputedCSV = list(map(float, imputedCSV))

	# 					refereceCSV = linecache.getline('accel_x_train_ref.csv',window)
	# 					refereceCSV = stringToList(refereceCSV)
	# 					refereceCSV = list(map(float, refereceCSV))

	# 					counter = 0
	# 					error = 0
	# 					normalizedError = 0
	# 					for point in imputedCSV:
	# 						error = error + ((refereceCSV[counter] - point)*(refereceCSV[counter] - point))
	# 						#normalizedError = normalizedError + (refereceCSV[counter]*refereceCSV[counter])
	# 						normalizedError = normalizedError + (point * point)
	# 						counter = counter + 1

						
	# 					filewriter.writerow([epoch, dimension1, dimension2, dimension3, window, error, error/normalizedError])


	#--------------------------------MSE and Average MSE--------------------------------------------


	# for epoch in epoches:
	# 	for dimension1 in dimensionsTested1:
	# 		for dimension2 in dimensionsTested2:				
	# 			for dimension3 in dimensionsTested3:
	# 				averageDimensionAccuracy = 0;
	# 				for windowsIndex in range(8):
	# 					AverageMSE = 0
	# 					percentDiff = 0
	# 					dimension = 0
	# 					size = 0
	# 					bestPercent = 100
	# 					bestPercentWindow = 0
	# 					string2 = "Mass run small architectures\\accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"
	# 					for currWindow in range(windows[windowsIndex], windows[windowsIndex+1] - 1):
	# 						# MSEsums = 0

	# 						imputedCSV = linecache.getline(string2, currWindow)
	# 						imputedCSV = stringToList(imputedCSV)
	# 						imputedCSV = list(map(float, imputedCSV))
	# 						dimension = len(imputedCSV)

	# 						refereceCSV = linecache.getline('accel_x_train_ref.csv', currWindow)
	# 						refereceCSV = stringToList(refereceCSV)
	# 						refereceCSV = list(map(float, refereceCSV))
	# 						meanToHundred = 1/statistics.mean(refereceCSV)
	# 						#refereceCSV = multiplyList(refereceCSV, meanToHundred)

	# 						#imputedCSV = multiplyList(imputedCSV, meanToHundred)


	# 						counter = 0
	# 						for point in imputedCSV:
	# 							percentDiff = percentDiff + (math.fabs(((refereceCSV[int(counter)] - point) / ((refereceCSV[int(counter)] + point)/2)))*100)
	# 							counter = counter + 1
	# 						# AverageMSE = AverageMSE + MSEsums/counter
	# 						if(bestPercent > percentDiff/counter):
	# 							bestPercentWindow = currWindow
	# 							bestPercent = percentDiff/counter
	# 						percentDiff = percentDiff / counter
	# 						AverageMSE = AverageMSE + mean_squared_error(refereceCSV, imputedCSV)

	# 					AverageMSE = AverageMSE / (windows[windowsIndex] - windows[windowsIndex+1] -1)

	# 					trainOrder = linecache.getline('train_order.csv', windows[windowsIndex])
	# 					trainOrder = stringToList(trainOrder)
	# 					trainOrder = list(map(float, trainOrder))
	# 					windowsIndex = windowsIndex + 1
	# 					size = 2*(dimension/dimension1) + dimension/dimension2 + dimension/dimension3
	# 					size = size * 4

	# 					filewriter.writerow([epoch, dimension1, dimension2, dimension3, trainOrder[1], trainOrder[2], math.fabs(AverageMSE), percentDiff, size, bestPercentWindow, bestPercent])
 


with open ('accel_x_dimension_accuracy.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile)
	filewriter.writerow(["Epochs", "d1", "d2", "d3", "Memory in bytes", "Activity 1","MSE",  "Activity 2","MSE", " ity 3", "MSE", "Activity 4", "MSE", "Activity 5", "MSE", "Activity 6","MSE",  "Activity 7", "MSE", "Activity 8", "MSE", "overall average", "MSE"])

	for epoch in epoches:
		for dimension1 in dimensionsTested1:
			for dimension2 in dimensionsTested2:				
				for dimension3 in dimensionsTested3:
					averageDimensionAccuracy = 0;
					activity1 = 0
					activity1MSE = 0
					activity2 = 0
					activity2MSE = 0
					activity3 = 0
					activity3MSE = 0
					activity4 = 0
					activity4MSE = 0
					activity5 = 0
					activity5MSE = 0
					activity6 = 0
					activity6MSE = 0
					activity7 = 0
					activity7MSE = 0
					activity8 = 0
					activity8MSE = 0
					percentDiff = 0
					MSE = 0
					for windowsIndex in range(8):
						for currWindow in range(windows[windowsIndex], windows[windowsIndex+1] - 1):
							string2 = "Mass run small architectures\\accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"

							imputedCSV = linecache.getline(string2, currWindow)
							imputedCSV = stringToList(imputedCSV)
							imputedCSV = list(map(float, imputedCSV))
							dimension = len(imputedCSV)

							refereceCSV = linecache.getline('accel_x_train_ref.csv', currWindow)
							refereceCSV = stringToList(refereceCSV)
							refereceCSV = list(map(float, refereceCSV))

							trainOrder = linecache.getline('train_order.csv', windows[windowsIndex])
							trainOrder = stringToList(trainOrder)
							trainOrder = list(map(float, trainOrder))

							counter = 0
							for point in imputedCSV:
								percentDiff = percentDiff + (math.fabs(((refereceCSV[int(counter)] - point) / ((refereceCSV[int(counter)] + point)/2)))*100)
								temp = (refereceCSV[counter] - point) * (refereceCSV[counter] - point)
								MSE = MSE + temp
								counter = counter + 1
							percentDiff = percentDiff/counter

						if trainOrder[2] == 1:
							activity1 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity1MSE = MSE/183
						if trainOrder[2] == 2:
							activity2 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity2MSE = MSE/183
						if trainOrder[2] == 3:
							activity3 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity3MSE = MSE/183
						if trainOrder[2] == 4:
							activity4 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity4MSE = MSE/183
						if trainOrder[2] == 5:
							activity5 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity5MSE = MSE/183
						if trainOrder[2] == 6:
							activity6 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity6MSE = MSE/183
						if trainOrder[2] == 7:
							activity7 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity7MSE = MSE/183
						if trainOrder[2] == 8:
							activity8 = percentDiff/(windows[windowsIndex + 1] - windows[windowsIndex])
							activity8MSE = MSE/183

					filewriter.writerow([epoch, dimension1, dimension2, dimension3, 2*(dimension/dimension1) + dimension/dimension2 + dimension/dimension3, activity1, activity1MSE, activity2, activity2MSE, activity3, activity3MSE, activity4, activity4MSE, activity5, activity5MSE, activity6, activity6MSE, activity7, activity7MSE, activity8, activity8MSE, (activity1+activity2+activity3+activity4+activity5+activity6+activity7+activity8)/8, (activity1MSE+activity2MSE+activity3MSE+activity4MSE+activity5MSE+activity6MSE+activity7MSE+activity8MSE)/8])




