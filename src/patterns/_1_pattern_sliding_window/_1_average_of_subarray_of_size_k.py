from typing import List

"""
// MNEMONIC - for loop with windowEnd from start to End, do necessary change in class level data, check if it passes the requirement, if not apply
// the while loop to increase windowStart and decrease windowSize , loopOut of whileLoop when the condition matches, and check the correct answer
/*
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Let’s understand this problem with a real input:

Array:[1,3,2,6,-1,4,1,8,2],K=5

Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:

1. For the first 5 numbers (subarray from index 0-4), the average is:(1+3+2+6-1)/5 => 2.2(1+3+2+6−1)/5=>2.2
2. The average of next 5 numbers (subarray from index 1-5) is:(3+2+6-1+4)/5 => 2.8(3+2+6−1+4)/5=>2.8
3. For the next 5 numbers (subarray from index 2-6), the average is:(2+6-1+4+1)/5 => 2.4(2+6−1+4+1)/5=>2.4

   …

Here is the final output containing the averages of all contiguous subarrays of size 5:

Output:[2.2,2.8,2.4,3.6,2.8]
 */
"""

"""
    Calculate the averages of all contiguous subarrays of size K.

    Parameters:
    K (int): The size of the subarrays for which the averages are to be calculated.
    arr (List[int]): The input list of integers from which the subarrays are derived.

    Returns:
    List[float]: A list containing the averages of the subarrays of size K.
                 If K is greater than the length of arr, an empty list is returned.

    Example:
    >>> find_averages(3, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    [2.0, 2.3333333333333335, 2.6666666666666665, 3.0, 4.0, 3.0]
"""
def find_averages(K: int, arr: List[int]) -> List[float]:
    if K <= 0 :
        raise ValueError('K must be greater than 0')
    elif K > len(arr):
        return []
    
    result = [0.0] * (len(arr) - K + 1)
    windowStart = 0
    windowEnd = 0
    windowSum = 0
    
    for i in range(len(arr)):
        windowSum += arr[i]
        if windowEnd >= (K - 1):
            result[windowStart] = windowSum / K
            windowSum -= arr[windowStart]    
            windowStart += 1
        windowEnd += 1
    
    return result

# Example usage
if __name__ == "__main__":
    result = find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K:", result)