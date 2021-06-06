import csv 
import math

with open("data.csv", newline='') as f:
  reader =  csv.reader(f)
  file_data = list(reader)

data = file_data[0]

def mean(data):
  total,no = 0,len(data)
  for i in data:
    total+= int(i)

  mean =  total/no
  print("mean is:", mean)
  return mean 


mean(data)

#sqr and get values
squaredlist=[]

for num in data :
  diff = int(num)- mean(data)
  sq = diff**2
  squaredlist.append(sq)

#getting sum
sum = 0
for i in squaredlist:
  sum= sum+i

# divide sum by total
result = sum/(len(data)- 1)

standard_Dev = math.sqrt(result)
print("standard deviation= ", standard_Dev)
