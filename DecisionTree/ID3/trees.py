from math import log
from collections import defaultdict


def createDataSet():
    """ the dataset for test """
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    # name of each feature
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    ''' the function is used to calculate Shannon Entropy, 
    a method to measure the disorder of data .
    the dataSet is like [[1,1,'yes'],[1,0,'no'],...]
    the last index of each vector stands for which class it belong.
    the feature needs to be discrete and numeric.
        return shannon Entropy
    '''

    numEntries = len(dataSet)
    # use lambda to define a function zero when key is not presented
    labelCounts = defaultdict(lambda: 0)
    for feaVec in dataSet:
        currentLabel = feaVec[-1]
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)  # -\sum [p*log(p)]
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    """split Dataset to get information gain for this axis
       axis means the fature to calculate using value 
       return the data splited
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducefeatVec = featVec[:]  # copy
            reducefeatVec.pop(axis)  # delete axis feature
            retDataSet.append(reducefeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    """ choose best feature according to information gain
        the data must have the same dimension
        return the feature chosen  
     """
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInforGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInforGain):
            bestInforGain = infoGain
            bestFeature = i
    return bestFeature


import operator


def majorityCnt(classList):
    """  this function is used when the algorithm cannot continue
    to classfy because all attributes are used
    majority of class will be chose.
        return the class chosen
    """
    classCount = defaultdict(lambda: 0)
    for vote in classList:
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    """ recursively calculate the tree 
        delete the label used
        return tree dictionary 
    """
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        # if all data is the same class, return
        return classList[0]
    if len(dataSet[0]) == 1:
        # if cannot continue, return
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    # init label
    myTree = {bestFeatLabel: {}}
    # have used the feature
    del(labels[bestFeat])
    # split the data according to feature value
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]  # copy
        myTree[bestFeatLabel][value] = createTree(splitDataSet
                                                  (dataSet, bestFeat, value), subLabels)
    return myTree



