import csv
import numpy

with open('List.csv', newline='') as csvfile:
     count = []
     rows = csv.reader(csvfile)   
     for row in rows:
         count.append(row[0])
     cc=numpy.unique(count).tolist()
     for c in cc:
         ac=count.count(c)
         print(c,ac)



