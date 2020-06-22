import matplotlib.pyplot as plt

seed = 3
a = 4
c = 1
m = 9

currentRandomNumber = seed
maxNumber = 10
randomNumberList = [currentRandomNumber]
randomIndexList = [0]

xAxisList = []
yAxisList = []

for index in range(0, maxNumber):
    currentRandomNumber = (currentRandomNumber * a + c) % m
    randomNumberList.append(currentRandomNumber)
    print(currentRandomNumber)
    randomIndexList.append(index)


for index in range(1, len(randomNumberList)):
    xAxisList.append(randomNumberList[index-1])
    yAxisList.append(randomNumberList[index])

plt.plot(xAxisList, yAxisList, 'b.')
plt.suptitle("'Bad' Random number generator")
plt.grid(True)
plt.show()
