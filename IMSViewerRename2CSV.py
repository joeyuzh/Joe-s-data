

import os, sys
import numpy as N

f = open('data1.csv','r')
	
data = N.loadtxt(f, delimiter = ',', skiprows = 1)
header = "mz,rt,int1, ,mz,rt,int2, ,mz,rt,int3, \n"
mzVals_1 = []
rtVals_1 = []
intVals_1 = []

eclCol = 3
intCol = 2

for i in xrange(len(data)):
	curRow = data[i]
	if curRow[2] >= curRow[3]:
		mzVals_1.append(curRow[0])
		rtVals_1.append(curRow[1])
		intVals_1.append(curRow[2])
f.close()

g = open('data2.csv','r')

data = N.loadtxt(g, delimiter = ',', skiprows = 1)
mzVals_2 = []
rtVals_2= []
intVals_2 = []

eclCol = 3
intCol = 2

for i in xrange(len(data)):
	curRow = data[i]
	if curRow[2] >= curRow[3]:
		mzVals_2.append(curRow[0])
		rtVals_2.append(curRow[1])
		intVals_2.append(curRow[2])
g.close()

h = open('data3.csv','r')

data = N.loadtxt(g, delimiter = ',', skiprows = 1)
mzVals_3 = []
rtVals_3= []
intVals_3 = []

eclCol = 3
intCol = 2

for i in xrange(len(data)):
	curRow = data[i]
	if curRow[2] >= curRow[3]:
		mzVals_3.append(curRow[0])
		rtVals_3.append(curRow[1])
		intVals_3.append(curRow[2])
h.close()

newFile = f.split('.')[0]
newFile+='_filter_group.csv'
nf = file(newFile, 'w')
nf.write(header)
len_com = max(len(mzVals_1),len(mzVals_2),len(mzVals_3) )
for j in xrange(len(len_com)):
	tempStr = mzVals_1[j]+rtVals_1[j]+intVals_1[j]+ " " +mzVals_2[j]+rtVals_2[j]+intVals_2[j]+" "+mzVals_3[j]+rtVals_3[j]+intVals_3[j]
	nf.write(tempStr)
nf.close()
#test github