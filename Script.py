import argparse
import numpy as np
import pandas as pd
import plotly_express as px
from timeit import default_timer as timer

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              nums[k] = left[i]
              i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k]=right[j]
            j += 1
            k += 1

def shellSort(nums):
    sublistcount = len(nums)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(nums, start_position, sublistcount)

      sublistcount = sublistcount // 2

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True



def heapify(nums, heap_size, root_index):
    
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2


    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            temp = items[j]
            items[j] = items[j - 1]
            items[j - 1] = temp
            j = j - 1


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def tim_sort(nums):
    nums.sort()



# Create file of numbers for sorting routines
def creator (num, dr):
    print(f"creator {num}, {dr}")
    rnumbers = [np.random.randint(1,999999, size=num)]
    rnumbersdf = pd.DataFrame(rnumbers)
    file = dr + '/numbers'
    rnumbersdf.T.to_csv(file, index = False, header = None)
    return file

def creatorSorted (num, dr):
    print(f"creatorSolved {num}, {dr}")
    snumbers = [np.random.randint(1,999999, size=num)]
    sorted = np.sort(snumbers)
    snumbersdf = pd.DataFrame(sorted)
    file = dr + '/numbers'
    snumbersdf.T.to_csv(file, index = False, header = None)
    return file

def creatorReversed (num, dr):
    print(f"creatorReversed {num}, {dr}")
    renumbers = [np.random.randint(1,999999, size=num)]
    sorted = np.sort(renumbers)
    reverseNum = np.flip(sorted)
    renumbersdf = pd.DataFrame(reverseNum)
    file = dr + '/numbers'
    renumbersdf.T.to_csv(file, index = False, header = None)
    return file

def creatorHalfpartition (num, dr):
    print(f"creatorReversed {num}, {dr}")
    Hfnumbers = [np.random.randint(1,999999, size=num)]
    sorted  = np.sort(Hfnumbers)
    Partnum = np.partition(sorted, int(num/2))
    renumbersdf = pd.DataFrame(Partnum)

    file = dr + '/numbers'
    renumbersdf.T.to_csv(file, index = False, header = None)
    return file

parser = argparse.ArgumentParser()
parser.add_argument('--sort', required = True)
args = parser.parse_args()
sortdr = args.sort
listOsorts = [quick_sort, ]
numsList = [5000, 10000, 100000]
df = pd.DataFrame(columns=['Time', 'Test', 'Sort'])


for num in numsList:
    file = creatorHalfpartition(num, sortdr)
    #nums = open(file).read().split()
    nums = pd.read_csv('numbers', names=['N'], dtype={'N': int}, header=None).N.to_list()
    #print(nums)
    for sorter in listOsorts:
        copyList = nums.copy()
        chartList = []
        start = timer()
        sorter(copyList)
        end = timer()
        final = (end - start)
        chartList.append(final)
        chartList.append(num)
        chartList.append(sorter.__name__)
        assert sorted(nums) == copyList #Test sort algo's actually worked
        df = df.append(pd.Series(chartList, index = df.columns[:len(chartList)]), ignore_index = True)

    
    
    

fig = px.line(df, x="Test", y="Time", color='Sort', markers=True)
fig.show()

print(df)    

