import os
import pandas as pd
import csv
#import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt 
#import pyplot as plt

file_to_rename = "stretch_imputed_train.csv"
print("-------------------------------------- stretch missing third layer 1 --------------------------------")
os.system("python gain.py -i stretch_missing_train.csv -o stretch_imputed_train.csv --T 1 --f 8 --s 2 --t 1 --testfile stretch_missing_test.csv")
os.rename(file_to_rename, "stretch_imputed_train_d3_1.csv")
print("-------------------------------------- stretch missing third layer 1 --------------------------------")


print()


print("-------------------------------------- stretch missing third layer 2 --------------------------------")
os.system("python gain.py -i stretch_missing_train.csv -o stretch_imputed_train.csv --T 1 --f 8 --s 2 --t 2 --testfile stretch_missing_test.csv")
os.rename(file_to_rename, "stretch_imputed_train_d3_2.csv")

print("-------------------------------------- stretch missing third layer 2 --------------------------------")


print()


print("-------------------------------------- stretch missing third layer 4 --------------------------------")
os.system("python gain.py -i stretch_missing_train.csv -o stretch_imputed_train.csv --T 1 --f 8 --s 2 --t 4 --testfile stretch_missing_test.csv")
os.rename(file_to_rename, "stretch_imputed_train_d3_4.csv")

print("-------------------------------------- stretch missing third layer 4 --------------------------------")


print()


print("-------------------------------------- stretch missing third layer 8 --------------------------------")
os.system(" python gain.py -i stretch_missing_train.csv -o stretch_imputed_train.csv --T 1 --f 8 --s 2 --t 8 --testfile stretch_missing_test.csv")
os.rename(file_to_rename, "stretch_imputed_train_d3_8.csv")
print("-------------------------------------- stretch missing third layer 8 --------------------------------")
print()