import random
import time 
import matplotlib.pyplot as plt 

max_size = 10000000
max_n = 100000
initial_size = 1000
count = 0

def generateRandomList(size, max_value):
    
    arr = []
    for _ in range(4):
        arr.append([random.randint(1, max_value) for _ in range(size)])
        size *= 10

    return arr

unsorted = generateRandomList(initial_size, max_n)
for i in unsorted: 
    print(len(i))
control = unsorted.copy()

def merge(arr,left, right):
    global count
    i = j = k = 0
    while i < len(left) and j < len(right):
        count+=1
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(arr, left, right)

def insertion_sort(arr):
    global count
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            count+=1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def hybrid_sort(arr, s):
    if len(arr) <= s:
        return insertion_sort(arr)
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    hybrid_sort(left, s)
    hybrid_sort(right, s)
    return merge(arr,left,right)

count=0
S = 10
results = []

input_array = unsorted[3].copy()

for s in range(5, 150, 5):

    total_time = 0
    count = 0    

    for _ in range(2):
    
        start_time = time.time()
        sorted_list = hybrid_sort(input_array, s)
        elapsed_time = time.time() - start_time
        total_time += elapsed_time

    results.append([s, count/10, total_time/10])
    print("Progress: " + str(s))
    
# Plotting Chart 

S = [row[0] for row in results]
time = [row[2] for row in results]
keycomp = [row[1] for row in results]

# Create the line graph
fig, ax1 = plt.subplots()

# Set the x-axis and primary y-axis labels
ax1.set_xlabel('S')
ax1.set_ylabel('time')

# Plot the primary y-axis data
ax1.plot(S, time, color='blue', label='time')

# Create the secondary y-axis
ax2 = ax1.twinx()

# Set the secondary y-axis label
ax2.set_ylabel('keycomp')

# Plot the secondary y-axis data
ax2.plot(S, keycomp, color='red', label='keycomp')

# Add a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='best')

# Show the plot
plt.show()