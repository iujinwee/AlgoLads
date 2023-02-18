# This doesnt work :(
import random
max_size = 100
max_n = 100
count = 0

def generateRandomList(size, max_value):
    return [random.randint(1, max_value) for _ in range(size)]

unsorted = generateRandomList(max_size, max_n)
control = unsorted.copy()

if unsorted == control:
	print("The control and unsorted are the same")

def merge (array, n, m):
	# n is first index, m is last index
	global count
	mid = (n + m) // 2
	a = n
	b = mid + 1
	if m - n <= 0:
		return
	
	while (a <= mid and b <= m):
		count += 1
		cmp = array [a] - array [b]
		if cmp > 0: 
			tmp = array[b]
			b += 1
			mid += 1
			for i in range (mid, a, -1):
				array[i] = array[i-1]
			array [a] = tmp
			a += 1

		elif cmp < 0:
			a += 1

		else:
			if a == mid and b == m:
				break
			tmp = array [b]
			b+=1
			a+=1
			mid += 1
			for i in range (mid, a, -1):
				array [i] = array[i-1]
			array [a] = tmp
			a += 1

def mergeSort(arr, l, r):
	mid = (l + r) // 2
	if (r - l) <= 0:
		return
	elif (r - l > 1):

		# Sort first and second halves
		mergeSort(arr, l, mid)
		mergeSort(arr, mid + 1, r)

	merge(arr, l, r)

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

def hybrid_sort(arr,n,m):
	if (m-n) <= 0:
		return
	elif (m-n) <= 10:
		insertion_sort(arr)
	else:
		mid = (n+m) // 2
		# Sort first and second halves
		hybrid_sort(arr, n, mid)
		hybrid_sort(arr, mid + 1, m)

	merge(arr, n, m)

count=0
S = 10
hybrid_sort(unsorted,0,max_size-1)
control = sorted(control)

# check that algo is correct

if sorted_list == control:
    print ("The control and sorted are the same")
else:
	print("The control and sorted are not the same")

print("Number of comparisons: {}".format(count))
print(sorted_list[:100])
print(control[:100])