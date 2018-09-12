#
# Longest Subarray Having Sum k
#
# Given an array of integers, determine the longest subarray whose elements
# sum to k.
#
# This optimal O(n) solution keeps a running sum. We map each running sum
# eg. sum(array[0..i]) to the first index where that sum occurs. Then we
# can simply check to see if the complement of the current running sum at j
# was mapped for some smaller i eg. array[0..i]. In that case your subarray
# sum is k in array[i..j], you have i (from map) and j to check length! Easy.
#
# Joel Rorseth
#

def longest_subarray(array, k):

    running_sum = 0
    longest = 0
    sum_lookup = {}

    for i in range(len(array)):

        running_sum += array[i]

        # Check for direct match from start index
        if running_sum == k:
            longest = i+1

        # Store first (further away) location where this sum occurs
        if running_sum not in sum_lookup:
            sum_lookup[running_sum] = i

        # See if the complement of running_sum was a previous sum at an index
        complement = running_sum - k
        if complement in sum_lookup:
            if (i - sum_lookup[complement]) > longest:
                longest = i - sum_lookup[complement]

    return longest



# Driver
a = [10,5,2,7,1,9]
b = [-5,8,-14,2,4,12]
print("Given", a, ", k =", 15, ", longest subarray has length", longest_subarray(a, 15))
print("Given", b, ", k =", -5, ", longest subarray has length", longest_subarray(b, -5))
