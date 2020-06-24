import matplotlib.pyplot as plt
import numpy.random as random

a = 25214903917
c = 11
m = 2 ** 48
seed = 10

maxNumber = 1000


def generateRandomNumberLinearCongruence():
    print("Generating list of random numbers using linear congruence method...")
    currentRandomNumber = seed
    randomNumberList = [seed]
    for index in range(0, maxNumber):
        currentRandomNumber = (currentRandomNumber * a + c) % m
        randomNumberList.append(currentRandomNumber)
        #print(currentRandomNumber)
    print("done.")
    return randomNumberList


def generateUniformRandomNumber(randomNumberList):
    print("scaling list of random numbers between 0 and 1...")
    uniformList = []
    for i in range(0, len(randomNumberList)):
        uniformList.append(randomNumberList[i] / m)
    print("done.")
    return uniformList


def generateRandomNumberNumPY():
    print("Generating list of random numbers using numPy...")
    randomNumberList = []
    for i in range(0, maxNumber):
        x = random.random_sample()
        randomNumberList.append(x)
    print("done.")
    return randomNumberList


def plotRandomNumberCorrelation(randomNumberList):
    print("plotting correlation between subsequently generated random numbers...")
    xAxisList = []
    yAxisList = []
    for index in range(1, len(randomNumberList)):
        xAxisList.append(randomNumberList[index-1])
        yAxisList.append(randomNumberList[index])
    plt.plot(xAxisList, yAxisList, 'b.')
    plt.suptitle("Correlation between element i and i-1\nusing 'good' linear congruence method")
    plt.xlabel("ri-1")
    plt.ylabel("ri")
    plt.grid(True)
    plt.show()
    print("done.")


def plotRandomNumberInOrder(randomNumberList):
    print("plotting random numbers in the order they were generated...")
    xAxisList = []
    yAxisList = []
    for index in range(0, len(randomNumberList)):
        xAxisList.append(index)
        yAxisList.append(randomNumberList[index])
    plt.plot(xAxisList, yAxisList, 'b.')
    plt.suptitle("Random numbers generated using 'good'\nlinear congruence method in order of their generation")
    plt.xlabel("i")
    plt.ylabel("ri")
    plt.grid(True)
    plt.show()
    print("done.")


def computePatternLength(randomNumberList):
    print("attempting to identify a repeating pattern...")
    firstHalfOfTheList = []
    secondHalfOfTheList = []
    patternRepeatFlag = False
    for index in range(0, len(randomNumberList)):
        #print("\nLooking for repetition in the first " + str(index) + " indices...")
        for i in range(0, index):
            if i < int(index/2):
                firstHalfOfTheList.append(randomNumberList[i])
            elif i >= int(index/2):
                secondHalfOfTheList.append(randomNumberList[i])

        if firstHalfOfTheList == secondHalfOfTheList:
            if len(firstHalfOfTheList) > 0:
                print('\033[1m' + "match found!" + '\033[0m' + " Pattern repeats every " + str(len(firstHalfOfTheList)) + " values!")
                print("firstHalfOfTheList: " + str(firstHalfOfTheList))
                print("secondHalfOfTheList: " + str(secondHalfOfTheList))
                patternRepeatFlag = True  # let the program know that the pattern does repeat
                return
        firstHalfOfTheList.clear()
        secondHalfOfTheList.clear()
    if patternRepeatFlag is False:
        print("No repeating pattern found.")
    print("done.")


def computePatternLengthWarnSubPatterns(randomNumberList):
    FirstHalfOfTheList = []
    secondHalfOfTheList = []
    repeatLength = []
    equalizedRepeatLength = []
    for index in range(0, len(randomNumberList)):
        for i in range(0, index):
            if i < int(index/2):
                FirstHalfOfTheList.append(randomNumberList[i])
            elif i >= int(index/2):
                secondHalfOfTheList.append(randomNumberList[i])

        if FirstHalfOfTheList == secondHalfOfTheList:
            if len(FirstHalfOfTheList) > 0:
                print("match found! Pattern repeats every " + str(len(FirstHalfOfTheList)) + " values!")
                print("FirstHalfOfTheList: " + str(FirstHalfOfTheList))
                print("secondHalfOfTheList: " + str(secondHalfOfTheList))
                repeatLength.append(len(FirstHalfOfTheList))
        FirstHalfOfTheList.clear()
        secondHalfOfTheList.clear()
    for i in range(0, len(repeatLength)):
        if i == 0:
            equalizedRepeatLength.append(repeatLength[i])
        else:
            equalizedRepeatLength.append(repeatLength[i] - repeatLength[i-1])
    for i in range(0, len(equalizedRepeatLength)):
        if equalizedRepeatLength[i] != equalizedRepeatLength[i-1]:
            print('\n' + '\033[1m' + '\033[91m' + "WARNING:" + '\033[0m' + " initial repeating pattern is itself a part of a larger pattern!")
            break


def computeUniformity(randomNumberList, k):
    print("computing uniformity of distribution for k = " + str(k) + "...")
    sequenceLength = len(randomNumberList)
    sumX = 0
    for i in range(0, sequenceLength):
        sumX = sumX + randomNumberList[i] ** k
    xK = (1 / sequenceLength) * sumX
    print("done.\nkth moment of distribution where k is " + str(k) + " is: " + str(xK))


'''
manualList = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5]
computePatternLengthWarnSubPatterns(manualList) # Use this to demonstrate the limitations of 'computePatternLength()
'''

uniformRandomList = generateUniformRandomNumber(generateRandomNumberLinearCongruence())
#uniformRandomList = generateRandomNumberNumPY()
computePatternLength(uniformRandomList)
plotRandomNumberCorrelation(uniformRandomList)
plotRandomNumberInOrder(uniformRandomList)
computeUniformity(uniformRandomList, 1)
computeUniformity(uniformRandomList, 2)

