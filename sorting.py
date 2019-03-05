"""
Name:   To Eun Kim
Module: COMP0005 Algorithms (18/19)
"""
import time
from random import randint
import sys
sys.setrecursionlimit(100000000)
from statistics import stdev

roundnum = 10

# Heap sorting algorithm
# heapCount is summation of the number of exchanges and comparison
heapCount = 0

def heapify(arr, n, i):
    global heapCount
    largest = i
    left = 2 * i + 1
    right = 2 * i + 1

    if left < n and arr[i] < arr[left]:
        heapCount += 1
        largest = left

    if right < n and arr[largest] < arr[right]:
        heapCount += 1
        largest = right
        heapify(arr, n, largest)


def heapSort(arr):
    global heapCount
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapCount += 1
        heapify(arr, i, 0)
    return heapCount

# --------------------------------------------------

# Quick sorting algorithm
# quickCount is summation of the number of exchanges and comparison
quickCount = 0

def partition(arr, low, high):
    global quickCount
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            quickCount += 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    quickCount += 1
    return i + 1

def quickSort(arr, low, high):
    global quickCount
    if low < high:
        quickCount += 1
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return quickCount

# ---------------------------------------------------------
# created nested list of list for appending random numbers
Randlist = []
for x in range(5):
    Randlist.append([])

# ---------------------------------------------------------
# <Heap Lists>
# created nested list for storing start times
heapStartTimeList = []
for x in range(5):
    heapStartTimeList.append([])

# created nested list for storing endtimes
heapEndTimeList = []
for x in range(5):
    heapEndTimeList.append([])

# created nested list for storing time taken for every round
heapRoundTimeList = []
for x in range(roundnum):
    heapRoundTimeList.append([])

heapAverageList = []
# ---------------------------------------------------------
# <QuickLists>

# created nested list for storing start times
quickStartTimeList = []
for x in range(10):
    quickStartTimeList.append([])

# created nested list for storing endtimes
quickEndTimeList = []
for x in range(10):
    quickEndTimeList.append([])

# created nested list for storing time taken for every round
quickRoundTimeList = []
for x in range(roundnum):
    quickRoundTimeList.append([])

quickAverageList = []

# --------------------------------------------------
# Automation of 10 rounds of heap sorting and quick sorting of 5 various input sizes


for p in range(roundnum):
    print("Round {} for graph {}".format(p + 1, p + 1))
    inputSize = 100_000
    i = 0
    while inputSize <= 10_000_000:
        p = 0
        for x in range(inputSize):
            Randlist[i].append(randint(0, inputSize))

        # Quick data collection---------------------------------
        print("Quick: Clock {} is ticking....".format(i + 1))

        quickStartTimeList[i] = time.time()
        print("Quick: The number of exchange and comparison for InputSize({}) is {} "
              .format(inputSize, quickSort(Randlist[i], 0, len(Randlist[i]) - 1)))
        quickEndTimeList[i] = time.time()

        quickTimeDifference = (quickEndTimeList[i] - quickStartTimeList[i])
        print("Quick: Time taken for InputSize({}) is {} second "
              .format(inputSize, quickTimeDifference))
        quickRoundTimeList[p].append(quickTimeDifference)
        print("\n")
        # -----------------------------------------------------------------

        # Heap data collection------------------------------
        print("Heap: Clock {} is ticking....".format(i + 1))

        heapStartTimeList[i] = time.time()
        print("Heap: The number of exchange and comparison for InputSize({}) is {} "
              .format(inputSize, heapSort(Randlist[i])))
        heapEndTimeList[i] = time.time()

        heapTimeDifference = (heapEndTimeList[i] - heapStartTimeList[i])
        print("Heap: Time taken for InputSize({}) is {} second ".format(inputSize, heapTimeDifference))
        heapRoundTimeList[p].append(heapTimeDifference)
        print("\n----------------\n")
        # -----------------------------------------------------------------



        inputSize = inputSize + 1100_000
        i = i + 1

# -------------------------------------------------------------

print("Quicksort Time list: \n", quickRoundTimeList)
print("\n")
print("Heapsort Time list: \n", heapRoundTimeList)
print("\n")

# -------------------------------------------------------------

# get average of Times of quicksort
for q in range(10):
    sumOfTime = 0
    for x in range(roundnum):
        sumOfTime = sumOfTime + quickRoundTimeList[x][q]

    avgOfTime = sumOfTime / 10
    print("Quick: Average Time of Clock({}) is {}".format(q + 1, avgOfTime))
    quickAverageList.append(avgOfTime)

# get standard deviation of quicksort data
print("Quick: Averages: ", quickAverageList)
quickStdev = stdev(quickAverageList)
print("Standard deviation of Quick Sorting is : ", quickStdev)

# -------------------------------------------------------------

# get average of Times of heapsort
for q in range(10):
    sumOfTime = 0
    for x in range(roundnum):
        sumOfTime = sumOfTime + heapRoundTimeList[x][q]

    avgOfTime = sumOfTime / 10
    print("Average Time of Clock({}) is {}".format(q + 1, avgOfTime))
    heapAverageList.append(avgOfTime)

# get standard deviation of heapsort data
print("Heap: Averages: ", heapAverageList)
heapStdev = stdev(heapAverageList)
print("Standard deviation of Heap Sorting is : ", heapStdev)
