import time
from random import randint

def heapify(arr, n, i): 
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	 

	if l < n and arr[i] < arr[l]: 
		largest = l 

	if r < n and arr[largest] < arr[r]: 
		largest = r 

	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i]

		heapify(arr, n, largest) 

def heapSort(arr): 
	n = len(arr) 

	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0) 

#--------------------------------------------------        
print("heap sort")
#created nested list of list for appending random numbers
randlist = []
for x in range(10):
    randlist.append([])

# created nested list for storing start times
startTimeList = []
for x in range(10):
    startTimeList.append([])

# created nested list for storing endtimes
endTimeList = []
for x in range(10):
    endTimeList.append([])

inputSize = 100000
i = 0
while(inputSize <= 10000000):

    for x in range(inputSize):
        num = randint(1, inputSize)
        randlist[i].append(num)

    print("Clock {} is ticking....".format(i+1))
    startTimeList[i] = time.time()
    heapSort(randlist[i])
    endTimeList[i] = time.time()
    print("Time taken for InputSize({}) is {} second ".format(inputSize, endTimeList[i] - startTimeList[i]))

    inputSize = inputSize + 1100000
    i = i + 1


'''
From 100k to 10M
1.  100000
2.  1200000
3.  2300000
4.  3400000
5.  4500000
6.  5600000
7.  6700000
8.  7800000
9.  8900000
10. 10000000
'''
