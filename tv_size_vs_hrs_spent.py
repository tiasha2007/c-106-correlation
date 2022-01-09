import csv
from typing import Dict
import numpy as np

def getDataSource(data_path):
    size_of_tv=[]
    avg_time_spent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            avg_time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))
        
    return {"X":size_of_tv, "Y":avg_time_spent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["X"],datasource["Y"])
    print("correlation between size of tv and average time spent watching in a week: \n--->",correlation[0,1])

def setup():
    data_path="size_of_tv_vs_hrs_spent_on_watching_tv.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
