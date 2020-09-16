# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    # pointers for array a and b
    a = 0
    b = 0

    # while the array's have elements
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1

        else:
            merged_arr.append(arrB[b])
            b += 1
    # elements merged in from one of the arrays, but not the other

    # check each array for leftovers
    if a < len(arrA):
        # push leftover elements to the merged array
        merged_arr.extend(arrA[a:])

    if b < len(arrB):
        # push leftover elements to the merged array
        merged_arr.extend(arrB[b:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # if less than 2 elements, there isn nothing to merge or sort
    if len(arr) < 2:
        return arr
    # if it's unsorted:
    else:
        # determine the midpoint,
        # and set our left and right arrays using that point
        midpoint = len(arr) // 2
        left = arr[0:midpoint]
        right = arr[midpoint:]
        # our finished array will be the result of a merge
        # between the recursive calls of merge sort which will return arrays when sorted
        arr = merge(merge_sort(left), merge_sort(right))
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
