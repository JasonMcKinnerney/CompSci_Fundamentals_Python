import numpy as np

# SIZE is a global constant, use this throughout your program.
# you should be able to change this to any int and your
# whole program will still work correctly. TEST THIS!
SIZE = 10

# initialize the array with 10, 20, 30, etc.
def make_array():
    # creates a numpy array of size SIZE filled with 0s.
    nums = np.array([0] * SIZE, dtype=int)
    
    # now fill it with 10,20,30, etc ***using a loop*** and return it
    for i in range(SIZE):
        nums[i] = (i + 1) * 10
    return nums

def calc_stats(nums):
    # make an integer array of size 4 to hold stats
    # calculate four basic stats and put them in the size 4 array in this order:
    # min, max, total, average
    # min and max will just be the first and last numbers from the nums array
    # average may calculate as a float, make it an int to store it in the stats array
    # return the stats array with all the correct stats in order
    stats = np.array([0] * 4, dtype=int)
    stats[0] = nums[0]
    stats[1] = nums[SIZE-1]

    total = 0
    for i in range(SIZE):
        total = total + nums[i]
    stats[2] = total
    stats[3] = total//SIZE

    return stats

def display_stats(stats):
    # make this display everything as shown in the examples
    # you can hard code the indexes, you don't need a loop
    print("Min: ", stats[0])
    print("Max: ", stats[1])
    print("Total: ", stats[2])
    print("Average: ", stats[3])    
    print()

def reverse_array(arr):
    # this will accept an integer array
    # put the numbers in another array in reverse order
    # and return the reversed array
    temp = np.array([0] * SIZE, dtype=int)
    
    j = SIZE-1
    for i in range(SIZE):
        temp[i] = arr[j]
        j -= 1
    
    return temp

def main():
    # this function is complete, DO NOT MODIFY IT
    # you may modify it while you program, but when you turn in for grading
    # it must be returned to EXACTLY this state
    
    # this will create and initialize the array with 10,20,30... etc
    numbers = make_array()
    
    # show the array
    print("All the numbers...")
    print(numbers)
    print()
    
    # this will calculate 4 stats, min, max, total, average
    statistics = calc_stats(numbers)
    
    # this will initialize the array with 10,20,30... etc
    display_stats(statistics)

    # this will reverse the array
    numbers = reverse_array(numbers)

    # show the array again
    print("All the numbers in reversed order...")
    print(numbers)
    print()

# this starts the program
# do not change this line
main()
