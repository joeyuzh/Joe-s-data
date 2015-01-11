

import os, sys
import numpy as N

for f in os.listdir('.'):
#f = 'F2014_04_15_10h25m00s.csv'
	data = N.loadtxt(f, delimiter = ',', skiprows = 1)
	header = "mz,rt,int\n"
	mzVals = []
	rtVals = []
	intVals = []

	eclCol = 3
	intCol = 2

	for i in xrange(len(data)):
		curRow = data[i]
		if curRow[2] >= curRow[3]:
			mzVals.append(curRow[0])
			rtVals.append(curRow[1])
			intVals.append(curRow[2])

	newFile = f.split('.')[0]
	newFile+='_filter.csv'
	nf = file(newFile, 'w')
	nf.write(header)
	for j in xrange(len(mzVals)):
		tempStr = "%s,%s,%s\n"%(mzVals[j], rtVals[j], intVals[j])
		nf.write(tempStr)
	nf.close()
