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




epoches = [3000]
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


with open('accel_x_accuracy.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile)
	filewriter.writerow(["Epochs", "d1", "d2", "d3", "missing percent", "Activity", "Average MSE"])




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


	for epoch in epoches:
		for dimension1 in dimensionsTested1:
			for dimension2 in dimensionsTested2:				
				for dimension3 in dimensionsTested3:
					for windowsIndex in range(8):
						AverageMSE = 0
						string2 = "Mass run small architectures\\accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"
						for currWindow in range(windows[windowsIndex], windows[windowsIndex+1] - 1):
							MSEsums = 0

							imputedCSV = linecache.getline(string2, currWindow)
							imputedCSV = stringToList(imputedCSV)
							imputedCSV = list(map(float, imputedCSV))

							refereceCSV = linecache.getline('accel_x_train_ref.csv', currWindow)
							refereceCSV = stringToList(refereceCSV)
							refereceCSV = list(map(float, refereceCSV))
							meanToHundred = 1/statistics.mean(refereceCSV)
							refereceCSV = multiplyList(refereceCSV, meanToHundred)

							imputedCSV = multiplyList(imputedCSV, meanToHundred)


							counter = 0
							for point in imputedCSV:
								MSEsums = MSEsums + ((refereceCSV[int(counter)] - point)*(refereceCSV[int(counter)] - point))
								counter = counter + 1
							AverageMSE = AverageMSE + MSEsums/counter

						AverageMSE = AverageMSE / (windows[windowsIndex] - windows[windowsIndex+1] -1)

						trainOrder = linecache.getline('train_order.csv', windows[windowsIndex])
						trainOrder = stringToList(trainOrder)
						trainOrder = list(map(float, trainOrder))
						windowsIndex = windowsIndex + 1

						filewriter.writerow([epoch, dimension1, dimension2, dimension3, trainOrder[1], trainOrder[2], math.fabs(AverageMSE)])
 











