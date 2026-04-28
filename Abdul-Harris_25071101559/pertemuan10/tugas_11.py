# DATA
data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510,443, 38, 505, 123,
        404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37,
        80, 0, 54, 14, 71,19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31,
        59, 98, 55, 99, 280, 303, 16, 25, 321]

print("Data sebelum sort:")
print(data)

# RADIX SORT 

def radixSort(arr):
    mylist = arr.copy()
    radixArray = [[], [], [], [], [], [], [], [], [], []]

    maxVal = max(mylist)
    exp = 1

    while maxVal // exp > 0:

        while len(mylist) > 0:
            val = mylist.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                mylist.append(val)

        exp *= 10

    return mylist

# MERGE SORT 

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# LINEAR SEARCH

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# BINARY SEARCH

def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# HASIL SORT

hasil_radix = radixSort(data)
print("\nHasil Radix Sort:")
print(hasil_radix)

hasil_merge = mergeSort(data)
print("\nHasil Merge Sort:")
print(hasil_merge)

# INPUT USER
x = int(input("\nMasukkan angka yang ingin dicari: "))

# Linear Search (data asli)
idx_linear = linearSearch(data, x)
if idx_linear != -1:
    print("\nLinear Search: ditemukan di index", idx_linear, "dengan nilai", data[idx_linear])
else:
    print("\nLinear Search: tidak ada")

# Binary Search (data sudah di-sort)
idx_binary = binarySearch(hasil_merge, x)
if idx_binary != -1:
    print("\nBinary Search: ditemukan di index", idx_binary, "dengan nilai", hasil_merge[idx_binary])
else:
    print("\nBinary Search: tidak ada")