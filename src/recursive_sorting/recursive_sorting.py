# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if (len(arrA) == 0):
            merged_arr[-len(arrB):] = arrB
        elif len(arrB) == 0:
            merged_arr[-len(arrA):] = arrA
        elif (arrA[0] > arrB[0]):
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
        else:
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = round(len(arr) / 2)
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
