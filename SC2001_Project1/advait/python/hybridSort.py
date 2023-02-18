import random
import functools
max_size = 100000
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

count=0
S = 10
sorted_list = hybrid_sort(unsorted,10)
control = sorted(control)

# check that algo is correct

if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,sorted_list,control), True):
    print ("The control and sorted are the same")

print("Number of comparisons: {}".format(count))
print(sorted_list[:100])
print(control[:100])