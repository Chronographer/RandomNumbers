import matplotlib.pyplot as plt

seed = 10
a = 57
c = 1
m = 256

currentRandomNumber = seed
maxNumber = 300
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
plt.xlabel("ri-1")
plt.ylabel("ri")
plt.grid(True)
plt.show()
