import csv
import numpy as np

def getDataSource(data_path):
    student_present=[]
    marks=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            student_present.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
        
    return {"X":student_present, "Y":marks}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["X"],datasource["Y"])
    print("correlation between students present vs marks in percentage: \n--->",correlation[0,1])

def setup():
    data_path="students_present_vs_marks.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
