import pickle
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

fileName = "stretch_analysis.csv"
data = open(fileName, 'r')

contents = data.readlines()
arr = []
numClusters = 4

try:
    kmeans = pickle.load(open("kmeans.pkl", 'rb'))
except FileNotFoundError:
    print("File not found")

try:
    for line in contents:
        line = (line.split(','))
        line = [float(x) for x in line]
        arr.append(line)

    labels = kmeans.labels_
    for index, label in enumerate(labels):
        c = ''
        if label == 0:
            c = 'red'
        elif label == 1:
            c = 'orange'
        elif label == 2:
            c = 'yellow'
        elif label == 3:
            c = 'green'
        plt.scatter(arr[index][0], arr[index][1], color=c)
    plt.show()
finally:
    data.close()
