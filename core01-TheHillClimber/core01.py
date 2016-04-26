# The Hill Climber - https://www.reddit.com/r/ludobots/wiki/core01

from __future__ import division

from copy import deepcopy

import matplotlib.cm as cm
import matplotlib.pyplot as fitnessPlot
import matplotlib.pyplot as genePlot


# Project Details:
# In this project, rather than evolving robots, you will simply evolve vectors of the form v = e1, . . . en, where the
# ith element in the vector may take on a real number in [0, 1]. The fitness of a vector v, denoted f(n) we will define
# as the mean value of all of its elements:

# Thus, the hill climber will search for vectors in which all of the elements have values near one. In a later project,
# you will re-use your hill climber to evolve artificial neural networks; in another project, you will use it to evolve
# robots.

# Let's get to work. The first step in the serial hill climber is to create a random vector. To do this, first create a
# Python function MatrixCreate(rows, columns). This function should return a rows by columns matrix with all elements
# set to zero. The vector we will use will actually be a 1 x 50 matrix. print MatrixCreate(1, 50) will show you whether
# your function works correctly or not.
def MatrixCreate(rows, columns):
    matrix = [[0 for x in xrange(columns)] for y in xrange(rows)]
    return matrix


# print MatrixCreate(1, 50)

# Create a function MatrixRandomize(v) that will put random values drawn from [0, 1] into each element of v. You'll need
# to use random.random(), which returns a random floating- point value in [0, 1].
import random


def MatrixRandomize(v):
    for row in xrange(len(v)):
        for col in xrange(len(v[row])):
            v[row][col] = random.random()

    return v


# The hill climber must now compute the fitness of the random vector. Create a function Fitness(v) that returns the mean
# value of all of the elements in v.
def Fitness(v):
    return sum(map(sum, v)) / (len(v) * len(v[0]))


# The hill climber must now create a modified copy of v. Create a function MatrixPerturb(p, prob) which makes a copy of
# the parent vector p, and then considers each element in the new vector c. (You may wish to make use of the function
# deepcopy in Python's copy library (i.e. copy.deepcopy ).) With probability prob, the element's value is replaced with
# a new random value drawn from [0, 1]; otherwise, the element's value is left as is. You can cause an event to happen
# with a given probability using an if statement: if prob > random.random():.
def MatrixPerturb(p, prob):
    c = deepcopy(p)
    for row in xrange(len(c)):
        for col in xrange(len(c[row])):
            if prob > random.random():
                c[row][col] = random.random()

    return c


# You can now use all of these functions to create a serial hill climber:
# You should see that as the fitness of parent is printed, the fitness value goes up as the generations pass.
def randomHillClimber():
    parent = MatrixCreate(1, 50)  # 1,50
    parent = MatrixRandomize(parent)
    parentFitness = Fitness(parent)

    fits = MatrixCreate(1, 5000)
    Genes = MatrixCreate(50, 5000)

    for currentGeneration in range(5000):
        # print currentGeneration, parentFitness
        for i in xrange(len(parent[0])):
            Genes[i][currentGeneration] = parent[0][i]

        fits[0][currentGeneration] = parentFitness
        child = MatrixPerturb(parent, 0.05)
        childFitness = Fitness(child)
        if childFitness > parentFitness:
            parent = child
            parentFitness = childFitness

    genePlot.imshow(Genes, cmap=cm.gray, aspect='auto', interpolation='nearest')
    genePlot.show()
    return fits


def multiHillClimber(runs):
    fits = MatrixCreate(runs, 5000)
    for run in xrange(runs):
        fits[run] = randomHillClimber()[0]

    return fits


# Deliverables:
# The first graph you will create will visually show how the fitness of the best vector climbs as the generations pass.
# In your existing code, create a new vector fits = MatrixCreate(1,5000) that stores the fitness value of the parent at
# each generation. Print fits after your code has run to make sure the fitness values have been stored.

# Create a function PlotVectorAsLine(fits) that plots the parent vector's fitness as a line (use plot() and show() from
# matplotlib). The graph should show one line with a curve, similar to the one in Fig. 1a. Save this figure to your
# computer.
fits = multiHillClimber(5)


def PlotVectorAsLine(fits):
    for run in xrange(len(fits)):
        fitnessPlot.plot(fits[run])

    fitnessPlot.xlabel('Generation')
    fitnessPlot.ylabel('Fitness')
    fitnessPlot.show()


# Wrap the Python code from step 8 above in a loop that runs the hill climber five times, each time starting with a
# different random vector. At the end of each pass through the loop, add another line to your graph, so that you have a
# picture similar to that in Fig. 1b. Save this figure to your computer.
PlotVectorAsLine(fits)

# Create a matrix Genes with 5000 columns and 50 rows. After each generation j of the hill climber, copy each element of
# the parent vector into the jth column of Genes. After the hill climber has run, print Genes to ensure the elements
# were stored correctly.

# The matplotlib function imshow(M) will print a matrix M as an image, where each pixel pij corresponds to element eij
# in M . Calling imshow(Genes, cmap=cm.gray, aspect='auto', interpolation='nearest') after the hill climber has
# terminated will produce a figure similar to that of Fig. 1c. (Note that you still have to call show() afterwards to
# display the graph) cmap=cm.gray will ensure that the image is shown in grayscale: elements with values near 1 will be
# plotted as near-white pixels; elements near zero will be plotted as near-black pixels. aspect='auto' will expand the
# otherwise very long, flat image to fill the figure window. interpolation='nearest' will stop any blurring between the
# pixels.
