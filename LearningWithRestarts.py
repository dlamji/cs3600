import NeuralNet as NN
import Testing

PenargList = []
CarargList = []

for _ in range(5):
	PenargList += [Testing.testPenData()[1]]
	CarargList += [Testing.testCarData()[1]]

PenStd = Testing.stDeviation(PenargList)
CarStd = Testing.stDeviation(CarargList)
PenAve = Testing.average(PenargList)
CarAve = Testing.average(CarargList)
PenMax = max(PenargList)
CarMax = max(CarargList)

print "testPenData:"
print "max:",PenMax
print "ave:",PenAve
print "std:",PenStd

print "\ntestCarData:"
print "max:",CarMax
print "ave:",CarAve
print "std:",CarStd