#######################
# Name: Jason McKinnerney
# Coding 05: Functions and Numpy Arrays
# Purpose: Take an array, calculate various stats on the array, and then reverse the array for multiple values
#######################

import numpy as np

SIZE = 10

def make_array():
    nums = np.array([0] * SIZE, dtype=int)
    for r in range(SIZE):
        nums[r] = (r+1)*10
    return(nums)



def calc_stats(nums):
    min = np.amin(nums)
    max = np.amax(nums)
    total = np.sum(nums)
    average = int(np.mean(nums))
    list = [min, max, total, average]
    stats = np.asarray(list, dtype = int)
    return(stats)


def display_stats(stats):
    print('Min:     ', stats[0])
    print('Max:     ', stats[1])
    print('Total:   ', stats[2])
    print('Average: ', stats[3])
    print()


def reverse_array(arr):
    rev = np.zeros(arr.size, dtype=int)
    for i in range(arr.size):
        rev[arr.size - (i+1)] = arr[i]
    return(rev)


def main():
    numbers = make_array()
    print("All the numbers...")
    print(numbers)
    print()
    statistics = calc_stats(numbers)
    display_stats(statistics)
    numbers = reverse_array(numbers)
    print("All the numbers in revered order...")
    print(numbers)
    print()

main()
