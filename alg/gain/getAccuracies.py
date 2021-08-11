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




epoches = [500, 1000, 1500, 2000, 2500, 3000, 3500]
windows = [2425, 2474, 2546, 2612, 2849, 2905, 2956, 2988]
dimensionsTested1 = [1, 2, 4, 8]
dimensionsTested2 = [1, 2, 4, 8]
dimensionsTested3 = [1, 2, 4, 8]

def stringToList(string):
    listRes = list(string.split(","))
    return listRes

# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])


with open('accel_x_accuracy.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile)
	filewriter.writerow(["Epochs", "d1", "d2", "d3", "window", "accuracy", "normalizedError"])




	for epoch in epoches:
		for dimension1 in dimensionsTested1:
			for dimension2 in dimensionsTested2:
				for dimension3 in dimensionsTested3:
					string2 = "accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"
					
					for window in windows:
						imputedCSV = linecache.getline(string2, window)
						imputedCSV = stringToList(imputedCSV)
						imputedCSV = list(map(float, imputedCSV))

						refereceCSV = linecache.getline('accel_x_train_ref.csv',window)
						refereceCSV = stringToList(refereceCSV)
						refereceCSV = list(map(float, refereceCSV))

						counter = 0
						error = 0
						normalizedError = 0
						for point in imputedCSV:
							error = error + ((refereceCSV[counter] - point)*(refereceCSV[counter] - point))
							#normalizedError = normalizedError + (refereceCSV[counter]*refereceCSV[counter])
							normalizedError = normalizedError + (point * point)
							counter = counter + 1

						
						filewriter.writerow([epoch, dimension1, dimension2, dimension3, window, error, error/normalizedError])










