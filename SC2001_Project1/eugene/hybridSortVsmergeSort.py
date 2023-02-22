import random
import time 
import matplotlib.pyplot as plt

max_size = 1000
max_n = 100000
count = 0

def generateRandomList(size, max_value):

    return [random.randint(1, max_value) for _ in range(size)]

unsorted = generateRandomList(max_size, max_n)
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


# S = 20
# runs = 5

# total_time = 0
# elapsed_time_HS = 0
# elapsed_time_MS = 0


# for _ in range(runs):
#     # hybridSort
#     input_array_HS = unsorted.copy()
#     start_time = time.time()
#     sorted_list = hybrid_sort(input_array_HS, S)
#     elapsed_time_HS += time.time() - start_time
#     print("{} - {}", _, elapsed_time_HS)

# count_HS = count/runs
# elapsed_time_HS/=runs
# count = 0

# for _ in range(runs):
#     # mergeSort
#     input_array_MS = unsorted.copy()
#     start_time = time.time()
#     sorted_list = mergeSort(input_array_MS)
#     elapsed_time_MS += time.time() - start_time
#     print("{} - {}", _, elapsed_time_MS)

# count_MS = count/runs
# elapsed_time_MS/=runs

# # Time Complexity Analysis
# print("\n== Time Complexity Comparisons ==")
# print("Performed on array size: {}".format(len(input_array_HS)))
# print("Change in Key Comparisons: {}".format(count_HS - count_MS))
# print("Time Improvement: {:.2%}".format(abs(elapsed_time_HS-elapsed_time_MS)/elapsed_time_HS))

# print("\n== hybridSort ==")
# print("The no. of key comparisons: {}".format(count_HS))
# print("The time taken (in ms): {:.2f} s".format(elapsed_time_HS))


# print("\n== mergeSort ==")
# print("The no. of key comparisons: {}".format(count_MS))
# print("The time taken (in ms): {:.2f} s".format(elapsed_time_MS))

S = 20
runs = 200
sizes = [generateRandomList(_, max_n) for _ in range(1000, 10000, 1000)]
HS_time = []
MS_time = []
IS_time = []


for size in sizes: 
    elapsed_time_IS = 0
    elapsed_time_HS = 0
    elapsed_time_MS = 0
    for _ in range(runs):
        print("{} {}".format(len(size), runs))
        
        temp_array = size.copy()
        start_time = time.time()
        hybrid_sort(temp_array, S)
        elapsed_time_HS += time.time() - start_time

        # temp_array = size.copy()
        # start_time = time.time()
        # insertion_sort(temp_array)
        # elapsed_time_IS += time.time() - start_time

        temp_array = size.copy()
        start_time = time.time()
        mergeSort(temp_array)
        elapsed_time_MS += time.time() - start_time

    MS_time.append(elapsed_time_MS/runs)
    HS_time.append(elapsed_time_HS/runs)
    IS_time.append(elapsed_time_IS/runs)

lab = [len(_) for _ in sizes]

plt.plot(lab, HS_time, label="hybridSort")
plt.plot(lab, MS_time, label='mergeSort')
# plt.plot(lab, IS_time, label='insertionSort')
plt.xlabel('Array Size')
plt.ylabel('Elapsed Run Time')
plt.legend()
plt.show()