import os
import pandas as pd
import csv
#import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt 
#import pyplot as plt

file_to_rename = "accel_x_imputed_train.csv"
print("-------------------------------------- stretch missing third layer 1 --------------------------------")
os.system("python gain.py -i accel_x_train.csv -o accel_x_imputed_train.csv --T 2 --f 1 --s 1 --t 1 --testfile accel_x_test.csv")
os.rename(file_to_rename, "accel_x_imputed_train_d3_1.csv")
print("-------------------------------------- stretch missing third layer 1 --------------------------------")


print()


print("-------------------------------------- stretch missing third layer 2 --------------------------------")
os.system("python gain.py -i accel_x_train.csv -o accel_x_imputed_train.csv --T 2 --f 1 --s 1 --t 2 --testfile accel_x_test.csv")
os.rename(file_to_rename, "accel_x_imputed_train_d3_2.csv")

print("-------------------------------------- stretch missing third layer 2 --------------------------------")


print()


print("-------------------------------------- stretch missing third layer 4 --------------------------------")
os.system("python gain.py -i accel_x_train.csv -o accel_x_imputed_train.csv --T 2 --f 1 --s 1 --t 4 --testfile accel_x_test.csv")
os.rename(file_to_rename, "accel_x_imputed_train_d3_4.csv")

print("-------------------------------------- stretch missing third layer 4 --------------------------------")


print()


print("-------------------------------------- stretch missing third layer 8 --------------------------------")
os.system("python gain.py -i accel_x_train.csv -o accel_x_imputed_train.csv --T 2 --f 1 --s 1 --t 8 --testfile accel_x_test.csv")
os.rename(file_to_rename, "accel_x_imputed_train_d3_8.csv")
print("-------------------------------------- stretch missing third layer 8 --------------------------------")
print()