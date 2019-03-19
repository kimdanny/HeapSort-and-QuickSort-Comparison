import matplotlib.pyplot as plt
import numpy

# 100K to 10M
Input_Size = [100_000, 1200_000, 2300_000, 3400_000, 4500_000,
              5600_000, 6700_000, 7800_000, 8900_000, 10_000_000]

# Heap Data
heapRun1 = [738530, 11644408, 23729241, 36317447, 49257226,
            62442549, 75840472, 89437678, 103104260, 116951122]
heapRun2 = [737631, 11645357, 23731999, 36325264, 49255898,
            62445644, 75834654, 89432148, 103103097, 116958672]
heapRun3 = [737490, 11644446, 23735331, 36320621, 49265581,
            62433885, 75839038, 89428109, 103109626, 116957249]
heapRun4 = [738111, 11649421, 23732171, 36317232, 49259663,
            62449814, 75836909, 89435057, 103104290, 116958079]
heapRun5 = [736549, 11645366, 23736392, 36317043, 49260659,
            62452466, 75832040, 89443687, 103107380, 116962610]
heapRun6 = [737457, 11645680, 23735020, 36315558, 49255845,
            62441184, 75831684, 89444202, 103109256, 116959430]
heapRun7 = [737281, 11649531, 23735765, 36320093, 49259551,
            62441555, 75836297, 89436721, 103102374, 116956336]
heapRun8 = [736379, 11645063, 23733770, 36322197, 49260673,
            62442055, 75838941, 89435324, 103114900, 116955049]
heapRun9 = [737381, 11647674, 23734398, 36326198, 49256666,
            62443824, 75836031, 89441034, 103105524, 116959478]
heapRun10 = [737481, 11643284, 23732160, 36316722, 49264184,
             62437592, 75838487, 89444630, 103105317, 116956111]

heapTenRuns = [heapRun1, heapRun2, heapRun3, heapRun4, heapRun5,
               heapRun6, heapRun7, heapRun8, heapRun9, heapRun10]

# Quick Data
quickRun1 = [165556, 2652886, 5579306, 8108330, 11469588,
             13720138, 16173762, 20984510, 22874960, 26339060]
quickRun2 = [152376, 2568882, 5538054, 7997676, 11095006,
             13999740, 16919460, 20031820, 24300816, 25339884]
quickRun3 = [150088, 2638522, 5517646, 7712888, 11239206,
             14173490, 17267116, 19172266, 23356742, 26481478]
quickRun4 = [181856, 2547960, 5656976, 8463464, 10504342,
             15383516, 16482726, 20884188, 22251620, 26504866]
quickRun5 = [183056, 2773240, 5842992, 8247712, 11239110,
             14350412, 16286036, 22822698, 22374280, 25257272]
quickRun6 = [168994, 2337894, 5830812, 8070484, 12527946,
             13647432, 17235534, 19965872, 22670026, 29692820]
quickRun7 = [160068, 2559314, 5615360, 7872322, 11236790,
             15080534, 18662844, 20728158, 22620358, 25131686]
quickRun8 = [160436, 2616516, 5078202, 9226270, 12163678,
             13997056, 17267864, 20092982, 24192396, 25624136]
quickRun9 = [158936, 2512706, 5418274, 8205806, 11433244,
             14388872, 17794968, 19134698, 22765816, 25137562]
quickRun10 = [166336, 2673148, 5371764, 8160588, 10493198,
              14641178, 18118552, 19844840, 22222392, 28253644]

quickTenRuns = [quickRun1, quickRun2, quickRun3, quickRun4, quickRun5,
                quickRun6, quickRun7, quickRun8, quickRun9, quickRun10]

# ------------------------------------------

# HEAP
HeapAverageCount = []
HeapStdCount = []
for x in range(10):
    temp = []
    for i in range(10):
        temp.append(heapTenRuns[i][x])
    HeapAverageCount.append(numpy.average(temp))
    HeapStdCount.append(numpy.std(temp))

# Debugging Purpose
print("Heap: count Average List: \n", HeapAverageCount)
print("Heap: count Standard Deviation List :\n", HeapStdCount)

# QUICK
QuickAverageCount = []
QuickStdCount = []
for x in range(10):
    temp = []
    for i in range(10):
        temp.append(quickTenRuns[i][x])
    QuickAverageCount.append(numpy.average(temp))
    QuickStdCount.append(numpy.std(temp))

# Debugging Purpose
print("Quick: count Average List: \n", QuickAverageCount)
print("Quick: count Standard Deviation List :\n", QuickStdCount)

fig = plt.figure()
plt.title('Average Comparisons and Exchanges with Standard Deviation')
plt.xlabel("Input Size")
plt.ylabel("Comparisons and Exchanges")
ax = plt.subplot(111)
ax.grid(alpha=0.5, linestyle=':')
ax.plot(Input_Size, HeapAverageCount, label='Heapsort')
ax.plot(Input_Size, QuickAverageCount, label='Quicksort')
ax.errorbar(Input_Size, HeapAverageCount, HeapStdCount,  capsize = 6)
ax.errorbar(Input_Size, QuickAverageCount, QuickStdCount,  capsize = 6)
plt.show()




