# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
import math
import copy
 
def loadCsv(filename):
	lines = csv.reader(open(r'diabetes.csv'))
	dataset = list(lines)
	classes=copy.copy(dataset[0:1])
	dataset=copy.copy(dataset[1:])
	
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset
 
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]
 
def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)

	return separated
 
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 #Desvio padrão 
def stdev(numbers): 
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)
 
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries
 
def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.items():
		summaries[classValue] = summarize(instances)
	
	
	return summaries
 
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	
	return bestLabel
	
 
def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	print(predictions,"\n")
	return predictions
	
 
def getAccuracy(testSet, predictions):
	correct = 0
	valorA=0
	valorB=0
	status=-1
	situacao=-1
	print(testSet[1],'\n')
	print(testSet[1][-1],"\n")
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct+=1
			if testSet[i][-1] ==1.0:
				valorA+=1
			elif testSet[i][-1] == 0.0:
				valorB+=1
	print(correct,"A",valorA,"B",valorB)
	if valorA>valorB:
		situacao=valorA
		status=1
	else:
		situacao=valorB
		status=0
		
	#Buscando qual a classe teve o maior acerto, acredito que estou no caminho certo, agora e fazer o teste final 
	accuracy=(correct/float(len(testSet))) * 100.0

	return accuracy,status
 
def main():
	filename = 'diabetes.csv'
	splitRatio = 0.67
	status=-1
	dataset = loadCsv(filename)
	trainingSet, testSet = splitDataset(dataset, splitRatio)
	print('Split {0} rows into train={1} and test={2} rows'.format(len(dataset), len(trainingSet), len(testSet)))
	# prepare model
	summaries = summarizeByClass(trainingSet)
	# test model
	predictions = getPredictions(summaries, testSet)
	accuracy,status = getAccuracy(testSet, predictions)
	print('Accuracy: {0}%'.format(accuracy))
	print("S",status)

 
main()