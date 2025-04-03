from typing import List

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