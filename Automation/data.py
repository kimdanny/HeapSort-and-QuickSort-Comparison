"""
<Reference>
1. Heap Sorting Algorithm
    URL: https://www.geeksforgeeks.org/heap-sort/

2. Quick Sorting Algorithm
    URL: https://www.geeksforgeeks.org/quick-sort/
"""
import time
from random import randint
import sys
sys.setrecursionlimit(1000000000)
import numpy

# Heap sorting algorithm
# heapCount is summation of the number of exchanges and comparison

def heapify(arr, n, i):
    global heapCount

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
        heapCount += 3

    if r < n and arr[largest] < arr[r]:
        largest = r
        heapCount += 3

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapCount += 2
        heapify(arr, n, largest)


def heapSort(arr):
    global heapCount
    n = len(arr)

    # Build max heap
    for i in range(n, 0, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]
        heapCount += 1

        heapify(arr, i, 0)

# def heapSort(arr):
#     numpy.sort(arr, kind='heapsort')

# --------------------------------------------------
# Quick sorting algorithm
# quickCount is summation of the number of exchanges and comparison

def partition(arr, low, high):
    global quickCount
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            quickCount += 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            quickCount += 1

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

# def quickSort(arr):
#     numpy.sort(arr, kind='quicksort')

# ---------------------------------------------------------
# initialise all the arrays and variables
inputSize = []

heapTimeList = []
quickTimeList = []

heapCountList = []
quickCountList = []
# ---------------------------------------------------------
# estimating all data
def estimateData():
    global heapCount
    global quickCount

    roundNum = 10
    for round in range(roundNum):
        randomList = []

        heapCount = 0
        quickCount = 0
        size = 100_000 + 1100_000 * round    # 100K to 10M
        inputSize.append(size)

        for x in range(size):
            randomList.append(randint(0, 1_000_000))
        copiedRandomList = randomList.copy()

        heapStartTime = time.time()
        heapSort(randomList)
        heapEndTime = time.time()
        heapTimeDifference = heapEndTime - heapStartTime
        heapTimeList.append(heapTimeDifference)
        heapCountList.append(heapCount)

        quickStartTime = time.time()
        quickSort(copiedRandomList)
        quickEndTime = time.time()
        quickTimeDifference = quickEndTime - quickStartTime
        quickTimeList.append(quickTimeDifference)
        quickCountList.append(quickCount)

# ---------------------------------------------------------
