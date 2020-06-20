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
import numpy
import matplotlib.pyplot as plt

#need this to call random number generator
from numpy.random import random_sample

npoints = 1000

#make pyplot plot.  If you don't have matplotlib, then comment this out
#and just print data out to use in Excel.

#Doing this one step at a time would be slow, but possible
print("Scalar method of generating random number sequence")
print("Uniform distribution")

ilist = []
xlist = []
for i in range(npoints):
    x = random_sample()
    ilist.append(i)
    xlist.append(x)
    #print (i, x)

plt.plot(ilist, xlist, color="red", label="list", linestyle="None",
         marker=".")

#generate sequence that is npoints long and store in an array
print("Array method of generating random number sequence")
print("Uniform distribution")

iarray = numpy.arange(0,npoints,1)  #array of integers
xarray = random_sample(npoints)     #array of random numbers

plt.plot(iarray, xarray, color="blue", label="array", linestyle="None",
         marker="x")

#other stuff for plot
plt.xlabel("i")
plt.xlabel("Number")
plt.legend()
plt.show()

######## Playing around -- delete for lab
#second_plot = gdisplay(xtitle='x_i+1',
#                       ytitle='x_i',
#                       width=500, height=500)
#crazy_correlations = gdots(color=color.green)
#
#for i in range(npoints-1):
#    rate(10000)
#    #print(xarray[i], xarray[i+1])
#    crazy_correlations.plot( pos=(xarray[i], xarray[i+1]) )
#
#print (numpy.average(xarray))
#print (numpy.var(xarray))
