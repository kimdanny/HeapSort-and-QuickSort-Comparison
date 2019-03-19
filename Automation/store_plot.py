from data import inputSize, heapTimeList, quickTimeList, \
    heapCountList, quickCountList, estimateData
import matplotlib.pyplot as plot

estimateData()
# writing data to files & store the list to list
with open("heapTimeStorage.txt", "a") as htimeFile:
    htimeFile.write('\n%s\n' % heapTimeList)
    htimeFile.close()

with open("quickTimeStorage.txt", "a") as qtimeFile:
    qtimeFile.write('\n%s\n' % quickTimeList)
    qtimeFile.close()

with open("heapCountStorage.txt", "a") as hcountFile:
    hcountFile.write('\n%s\n' % heapCountList)
    hcountFile.close()

with open("quickCountStorage.txt", "a") as qcountFile:
    qcountFile.write('\n%s\n' % quickCountList)
    qcountFile.close()

    # Graphing with data
    fig = plot.figure()
    plot.title('Runtime Estimation')
    plot.xlabel("Input Size")
    plot.ylabel("Runtime in seconds")
    ax = plot.subplot(111)
    ax.grid(alpha=0.5, linestyle=':')
    ax.plot(inputSize, heapTimeList, label='Heapsort')
    ax.plot(inputSize, quickTimeList, label='Quicksort')
    ax.legend()
    plot.show()

    fig = plot.figure()
    plot.title('Number of Comparisons and Exchanges')
    plot.xlabel("Input Size")
    plot.ylabel("Number of Comparisons and Exchanges")
    ax = plot.subplot(111)
    ax.grid(alpha=0.5, linestyle=':')
    ax.plot(inputSize, heapCountList, label='Heapsort')
    ax.plot(inputSize, quickCountList, label='Quicksort')
    ax.legend()
    plot.show()





















