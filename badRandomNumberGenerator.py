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
    #print("done.")
    return randomNumberList


def generateUniformRandomNumber(randomNumberList):
    print("scaling list of random numbers between 0 and 1...")
    uniformList = []
    for i in range(0, len(randomNumberList)):
        uniformList.append(randomNumberList[i] / m)
    #print("done.")
    return uniformList


def generateRandomNumberNumPY():
    print("Generating list of random numbers using numPy...")
    randomNumberList = []
    for i in range(0, maxNumber):
        x = random.random_sample()
        randomNumberList.append(x)
    #print("done.")
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
    #print("done.")


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
    #print("done.")


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
    #print("done.")


def computeUniformity(randomNumberList, k):
    print("computing uniformity of distribution for k=" + str(k) + "...")
    sequenceLength = len(randomNumberList)
    sumX = 0
    for i in range(0, sequenceLength):
        sumX = sumX + randomNumberList[i] ** k
    xK = (1 / sequenceLength) * sumX
    print("moment of distribution where k=" + str(k) + " is: " + str(xK))


uniformRandomList = generateUniformRandomNumber(generateRandomNumberLinearCongruence())
#uniformRandomList = generateRandomNumberNumPY()
computePatternLength(uniformRandomList)
plotRandomNumberCorrelation(uniformRandomList)
plotRandomNumberInOrder(uniformRandomList)
computeUniformity(uniformRandomList, 1)
computeUniformity(uniformRandomList, 2)

