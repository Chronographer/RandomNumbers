"""Create sequence of random numbers and plot with matplotlib.pyplot

Instructions:  to get true random numbers, you should import "numpy",
a number-crunching package on which visual is based.  Numpy has several
subpackages including "linalg" for doing linear algebra and "random"
for doing random number generation. To access high quality random
numbers you want to add
   import numpy.random

Here I am only using uniform float random numbers on the interval [0,1),
so I only import the routine "random_sample"  It can be used to generate
a single random number or a whole series of them.

Antonio Cancio
Phys 336/536
March 17, 2020
"""
import numpy as np
import matplotlib.pyplot as plt

maxPoints = 1000

# Doing this one step at a time would be slow, but possible
print("Scalar method of generating random number sequence\nUniform distribution")
iList = []
xList = []
for i in range(maxPoints):
    x = np.random.random_sample()
    iList.append(i)
    xList.append(x)
    # print(i, x)

plt.plot(iList, xList, color="red", label="list", linestyle="None", marker=".")

# generate sequence that is maxPoints long and store in an array
print("Array method of generating random number sequence\nUniform distribution")
iArray = np.arange(0, maxPoints, 1)  # array of integers
xArray = np.random.random_sample(maxPoints)  # array of random numbers

plt.plot(iArray, xArray, color="blue", label="array", linestyle="None", marker=".")

plt.ylabel("i")
plt.xlabel("Number")
plt.legend(loc="upper right", framealpha=0.96)
plt.show()
