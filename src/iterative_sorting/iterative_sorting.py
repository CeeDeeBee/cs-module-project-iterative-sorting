# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapping = True
    # Your code here
    while swapping:
        num_swaps = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                num_swaps += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]

        if num_swaps == 0:
            swapping = False

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
O(n)
'''


def counting_sort(arr, maximum=None):
    # Your code here
    # check if input is empty
    if not arr:
        return arr

    # find max val if not given
    if not maximum:
        maximum = max(arr) + 1

    # initialize buckets
    buckets = [0 for i in range(maximum+1)]

    # add counts to buckets and ensure no negative vals
    for i in arr:
        if i >= 0:
            buckets[i] += 1
        else:
            return "Error, negative numbers not allowed in Count Sort"

    # count up buckets to find indexes
    for i in range(1, len(buckets)):
        buckets[i] = buckets[i-1] + buckets[i]

    # create new array to put sorted vals in
    sorted_arr = [-1 for i in range(maximum)]

    # put vals in sorted array
    for i in arr:
        new_index = buckets[i]
        buckets[i] -= i
        sorted_arr[new_index-1] = i

    # return sorted array without placeholder vals
    return [i for i in sorted_arr if i >= 0]
