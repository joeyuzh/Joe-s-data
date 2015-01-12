#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as N
DELIM = '    '

f = open('data1.txt','r')
	
data = N.loadtxt(f, delimiter = DELIM, skiprows = 1)
header = "mz,rt,int1"+" "+"mz,rt,int2"+" "+"mz,rt,int3,\n"
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
print "Data 1 Done"

g = open('data2.txt','r')

data = N.loadtxt(g, delimiter = DELIM, skiprows = 1)
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
print "Data 2 Done"


h = open('data3.txt','r')

data = N.loadtxt(h, delimiter = DELIM, skiprows = 1)
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
print "Data 3 Done"

newFile = 'output'
newFile+='_filter_group.csv'
nf = file(newFile, 'w')
nf.write(header)
len_comp = N.array([len(mzVals_1),len(mzVals_2),len(mzVals_3)])
print len_comp
for j in xrange(len_comp.max()):
	if j<len(mzVals_1):
		tempStr1 = "%s,%s,%s"%(mzVals_1[j],rtVals_1[j],intVals_1[j])
	else:
		tempStr1 = ""

	if j<len(mzVals_2):
		tempStr2 = "%s,%s,%s"%(mzVals_2[j],rtVals_2[j],intVals_2[j])
	else:
		tempStr2 = ""

	if j<len(mzVals_3):
		tempStr3 = "%s,%s,%s"%(mzVals_3[j],rtVals_3[j],intVals_3[j])
	else:
		tempStr3 = ""
	tempStr = tempStr1+tempStr2+tempStr3+"\n"
	nf.write(tempStr)
nf.close()
#test github