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


#100, 200, 500, 1000, 1500, 2000, 2500, 3000, 4000, 5000
dimensionsTested2 = [8, 10, 12, 14, 16, 18, 20]
dimensionsTested3 = [10, 12, 14, 16, 18, 20]
epoches = [20000]



#------------------------------------------------------------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#####################################################################################################################################


file_to_rename = "accel_x_imputed_train.csv"

for epoch in epoches:
	for dimension2 in dimensionsTested2:
		for dimension3 in dimensionsTested3:
			print("-------------------------------------- accel_x_test epochs=" + str(epoch) + " 1st layer=4n" +" 2nd layer="+str(dimension2)+" 3rd layer=d/"+str(dimension3)+" --------------------------------")
			string1 = "python gain.py -i accel_x_train.csv -o accel_x_imputed_train.csv --it " + str(epoch) + " --T 2 --f 4"+ " --s " + str(dimension2) +" --t " + str(dimension3) + " --testfile accel_x_train.csv"
			os.system(string1)

# for epoch in epoches:
# 	for dimension2 in dimensionsTested2:
# 		for dimension3 in dimensionsTested3:
# 			print("-------------------------------------- accel_y_test epochs=" + str(epoch) + " 1st layer=4n"+" 2nd layer="+str(dimension2)+" 3rd layer=d/"+str(dimension3)+" --------------------------------")
# 			string1 = "python gain.py -i accel_z_train.csv -o accel_z_imputed_train.csv --it " + str(epoch) + " --T 4 --f 4" + " --s " + str(dimension2) +" --t " + str(dimension3) + " --testfile accel_z_test.csv"
# 			os.system(string1)

# for epoch in epoches:
# 	for dimension2 in dimensionsTested2:
# 		for dimension3 in dimensionsTested3:
# 			print("-------------------------------------- accel_z_test epochs=" + str(epoch) + " 1st layer=4n"+" 2nd layer="+str(dimension2)+" 3rd layer=d/"+str(dimension3)+" --------------------------------")
# 			string1 = "python gain.py -i accel_y_train.csv -o accel_y_imputed_train.csv --it " + str(epoch) + " --T 3 --f 4" + " --s " + str(dimension2) +" --t " + str(dimension3) + " --testfile accel_y_test.csv"
# 			os.system(string1)

# for epoch in epoches:
# 	for dimension2 in dimensionsTested2:
# 		for dimension3 in dimensionsTested3:
# 			print("-------------------------------------- stretch_test epochs=" + str(epoch) + " 1st layer=4n" + " 2nd layer="+str(dimension2)+" 3rd layer=d/"+str(dimension3)+" --------------------------------")
# 			string1 = "python gain.py -i stretch_train.csv -o stretch_train.csv --it " + str(epoch) + " --T 1 --f 4" + " --s " + str(dimension2) +" --t " + str(dimension3) + " --testfile stretch_train_test.csv"
# 			os.system(string1)
				# string2 = "accel_x_imputed_train_d1_" + str(dimension1) + "_d2_"+ str(dimension2) + "_d3_"+str(dimension3)+"_epoches_"+str(epoch)+".csv"
				# os.rename(file_to_rename, string2)
				# print("-------------------------------------- accel_x_test epochs=" + str(epoch) + " 1st layer=" + str(dimension1)+" 2nd layer="+str(dimension2)+" 3rd layer=d/"+str(dimension3)+" --------------------------------")
				# for plotWindow in windows: 
				# 	plt = None
				# 	imputedCSV = None
				# 	refereceCSV = None
				# 	missngCSV = None
				# 	train_order_csv = None
				# 	activity = None
				# 	missing_data_percent = None
				# 	import matplotlib.pyplot as plt
				# 	df = None
				# 	pltName = None
				# 	pd = None
				# 	import pandas as pd

				# 	imputedCSV = linecache.getline(string2, plotWindow)
				# 	imputedCSV = stringToList(imputedCSV)
				# 	imputedCSV = list(map(float, imputedCSV))

				# 	refereceCSV = linecache.getline('accel_x_train_ref.csv',plotWindow)
				# 	refereceCSV = stringToList(refereceCSV)
				# 	refereceCSV = list(map(float, refereceCSV))

				# 	missngCSV = linecache.getline('accel_x_train.csv',plotWindow) #csv.reader('stretch_missing_train.csv')
				# 	missngCSV = stringToList(missngCSV)
				# 	missngCSV = list(map(float, missngCSV))

				# 	train_order_csv = linecache.getline('train_order.csv', plotWindow)
				# 	train_order_csv = stringToList(train_order_csv)
				# 	train_order_csv = list(map(float, train_order_csv))
				# 	activity = train_order_csv[2]
				# 	missing_data_percent = train_order_csv[1]




				# 	df=pd.DataFrame({'x_values': range(1,184), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
				# 	plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
				# 	plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
				# 	plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
				# 	pltTitle = 'accel_x'+' missing_'+str(int(missing_data_percent*100))+' activity_'+str(int(activity))+' d1=' + str(dimension1) + ' d2='+ str(dimension2) + ' d3=' + str(dimension3) + ' window=' + str(plotWindow) + ' epoches' + str(epoch)
				# 	plt.title(pltTitle)
				# 	plt.legend()
				# 	#pltName = 'accel_x_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
				# 	#plt.set_title(pltName)
				# 	pltName = pltTitle+'.png'
				# 	plt.savefig(pltName, bbox_inches='tight', dpi = 300)

				# 	plt.clf()



#------------------------------------------------------------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#####################################################################################################################################

# file_to_rename = "accel_y_imputed_train.csv"



# for dimension in dimensionsTested:
# 	print("-------------------------------------- accel_y_test third layer d/"+str(dimension)+" --------------------------------")
# 	string1 = "python gain.py -i accel_y_train.csv -o accel_y_imputed_train.csv --T 3 --f 1 --s 1 --t " + str(dimension) + " --testfile accel_y_test.csv"
# 	os.system(string1)
# 	string2 = "accel_y_imputed_train_d3_"+str(dimension)+".csv"
# 	os.rename(file_to_rename, string2)
# 	print("-------------------------------------- accel_y_test third layer d/"+str(dimension)+" --------------------------------")
# 	for plotWindow in windows:
# 		plt = None
# 		imputedCSV = None
# 		refereceCSV = None
# 		missngCSV = None
# 		train_order_csv = None
# 		activity = None
# 		missing_data_percent = None
# 		import matplotlib.pyplot as plt
# 		df = None
# 		pltName = None
# 		pd = None
# 		import pandas as pd

# 		imputedCSV = linecache.getline('accel_y_imputed_train_d3_'+str(dimension)+'.csv',plotWindow)
# 		imputedCSV = stringToList(imputedCSV)
# 		imputedCSV = list(map(float, imputedCSV))

# 		refereceCSV = linecache.getline('accel_y_train_ref.csv',plotWindow)
# 		refereceCSV = stringToList(refereceCSV)
# 		refereceCSV = list(map(float, refereceCSV))

# 		missngCSV = linecache.getline('accel_y_train.csv',plotWindow) #csv.reader('stretch_missing_train.csv')
# 		missngCSV = stringToList(missngCSV)
# 		missngCSV = list(map(float, missngCSV))

# 		train_order_csv = linecache.getline('train_order.csv', plotWindow)
# 		train_order_csv = stringToList(train_order_csv)
# 		train_order_csv = list(map(float, train_order_csv))
# 		activity = train_order_csv[2]
# 		missing_data_percent = train_order_csv[1]




# 		df=pd.DataFrame({'x_values': range(1,184), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
# 		plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
# 		plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
# 		plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
# 		plt.legend()
# 		pltName = 'accel_y_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
# 		#plt.set_title(pltName)
# 		pltName = pltName+'.png'
# 		plt.savefig(pltName, bbox_inches='tight', dpi = 300)

# 		plt.clf()


#------------------------------------------------------------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#####################################################################################################################################

# file_to_rename = "accel_z_imputed_train.csv"


# for dimension in dimensionsTested:
# 	print("-------------------------------------- accel_z_test third layer d/"+str(dimension)+" --------------------------------")
# 	string1 = "python gain.py -i accel_z_train.csv -o accel_z_imputed_train.csv --T 4 --f 1 --s 1 --t " + str(dimension) + " --testfile accel_z_test.csv"
# 	os.system(string1)
# 	string2 = "accel_z_imputed_train_d3_"+str(dimension)+".csv"
# 	os.rename(file_to_rename, string2)
# 	print("-------------------------------------- accel_z_test third layer d/"+str(dimension)+" --------------------------------")
# 	for plotWindow in windows:
# 		plt = None
# 		imputedCSV = None
# 		refereceCSV = None
# 		missngCSV = None
# 		train_order_csv = None
# 		activity = None
# 		missing_data_percent = None
# 		import matplotlib.pyplot as plt
# 		df = None
# 		pltName = None
# 		pd = None
# 		import pandas as pd

# 		imputedCSV = linecache.getline('accel_z_imputed_train_d3_'+str(dimension)+'.csv',plotWindow)
# 		imputedCSV = stringToList(imputedCSV)
# 		imputedCSV = list(map(float, imputedCSV))

# 		refereceCSV = linecache.getline('accel_z_train_ref.csv',plotWindow)
# 		refereceCSV = stringToList(refereceCSV)
# 		refereceCSV = list(map(float, refereceCSV))

# 		missngCSV = linecache.getline('accel_z_train.csv',plotWindow) #csv.reader('stretch_missing_train.csv')
# 		missngCSV = stringToList(missngCSV)
# 		missngCSV = list(map(float, missngCSV))

# 		train_order_csv = linecache.getline('train_order.csv', plotWindow)
# 		train_order_csv = stringToList(train_order_csv)
# 		train_order_csv = list(map(float, train_order_csv))
# 		activity = train_order_csv[2]
# 		missing_data_percent = train_order_csv[1]




# 		df=pd.DataFrame({'x_values': range(1,184), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
# 		plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
# 		plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
# 		plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
# 		plt.legend()
# 		pltName = 'accel_z_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
# 		#plt.set_title(pltName)
# 		pltName = pltName+'.png'
# 		plt.savefig(pltName, bbox_inches='tight', dpi = 300)

# 		plt.clf()



#------------------------------------------------------------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#####################################################################################################################################

# file_to_rename = "stretch_imputed_train.csv"


# for dimension in dimensionsTested:
# 	print("-------------------------------------- stretch_test third layer d/"+str(dimension)+" --------------------------------")
# 	string1 = "python gain.py -i stretch_missing_train.csv -o stretch_imputed_train.csv --T 1 --f 1 --s 1 --t " + str(dimension) + " --testfile stretch_missing_test.csv"
# 	os.system(string1)
# 	string2 = "stretch_imputed_train_d3_"+str(dimension)+".csv"
# 	os.rename(file_to_rename, string2)
# 	print("-------------------------------------- stretch_test third layer d/"+str(dimension)+" --------------------------------")
# 	for plotWindow in windows:
# 		plt = None
# 		imputedCSV = None
# 		refereceCSV = None
# 		missngCSV = None
# 		train_order_csv = None
# 		activity = None
# 		missing_data_percent = None
# 		import matplotlib.pyplot as plt
# 		df = None
# 		pltName = None
# 		pd = None
# 		import pandas as pd

# 		imputedCSV = linecache.getline('stretch_imputed_train_d3_'+str(dimension)+'.csv',plotWindow)
# 		imputedCSV = stringToList(imputedCSV)
# 		imputedCSV = list(map(float, imputedCSV))

# 		refereceCSV = linecache.getline('stretch_ref_train.csv',plotWindow)
# 		refereceCSV = stringToList(refereceCSV)
# 		refereceCSV = list(map(float, refereceCSV))

# 		missngCSV = linecache.getline('stretch_missing_train.csv',plotWindow) #csv.reader('stretch_missing_train.csv')
# 		missngCSV = stringToList(missngCSV)
# 		missngCSV = list(map(float, missngCSV))

# 		train_order_csv = linecache.getline('train_order.csv', plotWindow)
# 		train_order_csv = stringToList(train_order_csv)
# 		train_order_csv = list(map(float, train_order_csv))
# 		activity = train_order_csv[2]
# 		missing_data_percent = train_order_csv[1]




# 		df=pd.DataFrame({'x_values': range(1,73), 'reference': refereceCSV, 'imputed': imputedCSV, 'missing': missngCSV})
# 		plt.plot( 'x_values', 'reference', data=df, marker='', markerfacecolor='blue',  linewidth=2)
# 		plt.plot( 'x_values', 'imputed', data=df, marker='', color='olive', linewidth=2)
# 		plt.plot( 'x_values', 'missing', data=df, marker='', color='red', linewidth=2)#, label="toto")
# 		plt.legend()
# 		pltName = 'stretch_d3_'+str(dimension)+'_missing_'+str(missing_data_percent)+'_activity_'+str(activity)
# 		#plt.set_title(pltName)
# 		pltName = pltName+'.png'
# 		plt.savefig(pltName, bbox_inches='tight', dpi = 300)

# 		plt.clf()







