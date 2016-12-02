from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import random

def getNNxorData(fileString="datasets/xordigits.txt", limit=100000):
    """
    returns limit # of examples from penDigits file
    """
    examples=[]
    data = open(fileString)
    lineNum = 0
    for line in data:
        inVec = [0,0]
        outVec = [0,0]                      #which digit is output
        count=0
        for val in line.split(','):
            if count==2:
                outVec[int(val)] = 1
            else:
                inVec[count] = int(val)              #need to normalize values for inputs
            count+=1
        examples.append((inVec,outVec))
        lineNum += 1
        if (lineNum >= limit):
            break
    return examples

def buildExamplesFromxorData(size=10000):
    """
    build Neural-network friendly data struct
            
    pen data format
    16 input(attribute) values from 0 to 100
    10 possible output values, corresponding to a digit from 0 to 9

    """
    if (size != 10000):
        penDataTrainList = getNNxorData("datasets/xorTrain.txt",int(.8*size))
        penDataTestList = getNNxorData("datasets/xorTest.txt",int(.2*size))
    else :    
        penDataTrainList = getNNxorData("datasets/xorTrain.txt")
        penDataTestList = getNNxorData("datasets/xorTest.txt")
    return penDataTrainList, penDataTestList

xorData = buildExamplesFromxorData();
def testxorData(hiddenLayers = [24], mI = 200):
    return buildNeuralNet(xorData,maxItr = mI, hiddenLayerList =  hiddenLayers)

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

xorargList = []
for _ in range(5):
	# change testxordata([_]) for q7
	# for [2], it's still possible to fail to generate a good net
	# for [3], it can guarantee to generate a good net
	xorargList += [testxorData([0],400)[1]]

xorStd = stDeviation(xorargList)
xorAve = average(xorargList)
xorMax = max(xorargList)

print "testxorData:"
print "max:",xorMax
print "ave:",xorAve
print "std:",xorStd

