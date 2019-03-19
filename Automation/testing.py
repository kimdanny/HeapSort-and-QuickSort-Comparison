from random import randint
import numpy

randomList = []
size = 100_000 + 1100_000 * 5
for x in range(size):
    randomList.append(randint(0, 1_000_000))

# See how many repetitions of elements in a single list
a = numpy.array(randomList)
unique, counts =numpy.unique(a, return_counts=True)
this = dict(zip(unique, counts))
print(this)
