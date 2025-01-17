 # The main advantage of the bubble sort algorithm is its simplicity. 
 # It is straightforward to both implement and understand. This is 
 # probably the main reason why most computer science courses introduce
 # the topic of sorting using bubble sort.

# the disadvantage of bubble sort is that it is slow, with a runtime 
# complexity of O(n2). Unfortunately, this rules it out as a practical
# candidate for sorting large arrays.

from random import randint

def bubble_sort(arr):
    a = arr
    n = len(arr)
    
    # An outer loop that controls how many times the inner loop must run
    # For an array with n values, this outer loop must run n-1 times
    for i in range(n-1): 
        # To improve efficiency should the array be almost sorted already...
        # We can recognize and opportunity to distrupt processing and break out of loop
        swapped = False
        # An inner loop that goes through the array and swaps values if the first value is higher than the next value
        # This loop must loop through one less value each time it runs
        for j in range(n-i-1):
            # If next index value is greater than current index value, swap values around
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        # If we went through the whole array and didn't swap, we can break
        if not swapped:
            break
    return a


unsorted_arr = [1, 6, 2, 9, 5, 7, 2, 4, 0, 14, 2, 15, 17, 2, 45]
print(f"Unsorted list is: {unsorted_arr}")
sorted_arr = bubble_sort(unsorted_arr)
print(f"Sorted list is: {sorted_arr}")

# Generate an array of `ARRAY_LENGTH` items consisting
# of random integer values between 0 and 999
ARRAY_LENGTH = 100
random_arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
print(f"Unsorted list is: {random_arr}")
sorted_arr = bubble_sort(random_arr)
print(f"Sorted list is: {sorted_arr}")
