import matplotlib.pyplot as plt
import color

a = 57
c = 1
m = 256
seed = 10

maxNumber = 1000
xAxisList = []
yAxisList = []


def generateRandomNumberLinearCongruence():
    currentRandomNumber = seed
    randomNumberList = [seed]
    for index in range(0, maxNumber):
        currentRandomNumber = (currentRandomNumber * a + c) % m
        randomNumberList.append(currentRandomNumber)
        # print(currentRandomNumber)
    return randomNumberList


def plotRandomNumberCorrelation(randomNumberList):
    for index in range(1, len(randomNumberList)):
        xAxisList.append(randomNumberList[index-1])
        yAxisList.append(randomNumberList[index])
    plt.plot(xAxisList, yAxisList, 'b.')
    plt.suptitle("'Bad' Random number generator")
    plt.xlabel("ri-1")
    plt.ylabel("ri")
    plt.grid(True)
    plt.show()


def computePatternLength(randomNumberList):
    print("\nNOTE: This program does not account for the possibility that the first instance of a repeating pattern is not itself a part of a larger pattern.\nTry re-running 'computePatternLength()' using 'manualList' as an argument for details.\n")
    comparisonList = []
    secondHalfOfTheList = []
    for index in range(0, len(randomNumberList)):
        print("\nLooking for repetition in the first " + str(index) + " indices...")
        for i in range(0, index):
            if i < int(index/2):
                comparisonList.append(randomNumberList[i])
            elif i >= int(index/2):
                secondHalfOfTheList.append(randomNumberList[i])

        if comparisonList == secondHalfOfTheList:
            if len(comparisonList) > 0:
                print("match found! Pattern repeats every " + str(len(comparisonList)) + " values!")
                print("comparisonList: " + str(comparisonList))
                print("secondHalfOfTheList: " + str(secondHalfOfTheList))
                return
        comparisonList.clear()
        secondHalfOfTheList.clear()

def computePatternLengthWarnSubPatterns(randomNumberList):
    comparisonList = []
    secondHalfOfTheList = []
    repeatLength = []
    equilizedRepeatLength = []
    for index in range(0, len(randomNumberList)):
        #print("\nLooking for repetition in the first " + str(index) + " indices...")
        for i in range(0, index):
            if i < int(index/2):
                comparisonList.append(randomNumberList[i])
            elif i >= int(index/2):
                secondHalfOfTheList.append(randomNumberList[i])

        if comparisonList == secondHalfOfTheList:
            if len(comparisonList) > 0:
                print("match found! Pattern repeats every " + str(len(comparisonList)) + " values!")
                print("comparisonList: " + str(comparisonList))
                print("secondHalfOfTheList: " + str(secondHalfOfTheList))
                repeatLength.append(len(comparisonList))
                #return
        comparisonList.clear()
        secondHalfOfTheList.clear()
    for i in range(0, len(repeatLength)):
        if i == 0:
            equilizedRepeatLength.append(repeatLength[i])
        else:
            equilizedRepeatLength.append(repeatLength[i] - repeatLength[i-1])
    for i in range(0, len(equilizedRepeatLength)):
        if equilizedRepeatLength[i] != equilizedRepeatLength[i-1]:
            print('\n' + '\033[1m' + '\033[91m' + "WARNING:" + '\033[0m' + " initial repeating pattern is itself a part of a larger pattern!")
            break


manualList = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5, 1, 2, 3, 1, 2, 3, 5]  # Use this to demonstrate the limitations of 'computePatternLength()'
#computePatternLengthWarnSubPatterns(manualList)
computePatternLength(generateRandomNumberLinearCongruence())
