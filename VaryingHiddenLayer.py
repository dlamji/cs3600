import Testing
from time import time

CarPlot = []
PenPlot = []
CarAve = []
PenAve = []
CarStd = []
PenStd = []
CarMax = []
PenMax = []

t0 = time()
for i in range(1,9):
	tmpPen = []
	tmpCar = []
	for _ in range(5):
		tmpPen += [Testing.testPenData([5*i])[1]]
		tmpCar += [Testing.testCarData([5*i])[1]]
	PenAve += [Testing.average(tmpPen)]
	CarAve += [Testing.average(tmpCar)]
	PenStd += [Testing.stDeviation(tmpPen)]
	CarStd += [Testing.stDeviation(tmpCar)]
	PenMax += [max(tmpPen)]
	CarMax += [max(tmpCar)]

	PenPlot += [tuple([5*i,PenAve[i-1]])]
	CarPlot += [tuple([5*i,CarAve[i-1]])]

t1 = time()
print "Total time spent: ", t1-t0

print "\ntestPenData:"
print "max:",PenMax
print "ave:",PenAve
print "std:",PenStd

print "\ntestCarData:"
print "max:",CarMax
print "ave:",CarAve
print "std:",CarStd

print "\nPenData array: ",PenPlot
print "\nCarData array: ",CarPlot