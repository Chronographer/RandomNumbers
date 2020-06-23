import matplotlib.pyplot as plt

a = 57
c = 1
m = 256
seed = 10

maxNumber = 1000


def generateRandomNumberLinearCongruence():
    currentRandomNumber = seed
    randomNumberList = [seed]
    for index in range(0, maxNumber):
        currentRandomNumber = (currentRandomNumber * a + c) % m
        randomNumberList.append(currentRandomNumber)
        # print(currentRandomNumber)
    return randomNumberList


def plotRandomNumberCorrelation(randomNumberList):
    xAxisList = []
    yAxisList = []
    for index in range(1, len(randomNumberList)):
        xAxisList.append(randomNumberList[index-1])
        yAxisList.append(randomNumberList[index])
    plt.plot(xAxisList, yAxisList, 'b.')
    plt.suptitle("'Bad' Random number generator")
    plt.xlabel("ri-1")
    plt.ylabel("ri")
    plt.grid(True)
    plt.show()


def plotRandomNumberInOrder(randomNumberList):
    xAxisList = []
    yAxisList = []
    for index in range(0, len(randomNumberList)):
        xAxisList.append(index)
        yAxisList.append(randomNumberList[index])
    plt.plot(xAxisList, yAxisList, 'b.')
    plt.suptitle("'Bad' Random number generator")
    plt.xlabel("i")
    plt.ylabel("ri")
    plt.grid(True)
    plt.show()


def computePatternLength(randomNumberList):
    print("\nNOTE: This program does not account for the possibility that the first instance of a repeating pattern is not itself a part of a larger pattern.\nTry re-running 'computePatternLength()' using 'manualList' as an argument for details.\n")
    firstHalfOfTheList = []
    secondHalfOfTheList = []
    for index in range(0, len(randomNumberList)):
        # print("\nLooking for repetition in the first " + str(index) + " indices...")
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
                return
        firstHalfOfTheList.clear()
        secondHalfOfTheList.clear()


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


'''
manualList = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5]
computePatternLengthWarnSubPatterns(manualList) # Use this to demonstrate the limitations of 'computePatternLength()
'''
randomList = generateRandomNumberLinearCongruence()
computePatternLength(randomList)
plotRandomNumberCorrelation(randomList)
plotRandomNumberInOrder(randomList)
