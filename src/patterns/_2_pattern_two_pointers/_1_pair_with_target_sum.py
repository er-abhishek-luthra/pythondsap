from typing import List, Tuple

"""
Problem Statement #
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


class PairWithTargetSum():

    @staticmethod
    def find_pair_with_target_sum(arr: List[int], targetSum:int) -> Tuple[int,int] :
        """
        Finds a pair of indices in the sorted array that sum up to the targetSum

        Parameters:
        arr (List[int]): A list of integers ( must contain at least two elements).
        targetSum (int) : The target sum to find

        Returns:
        Tuple[int,int]: A tuple of indices of the two numbers that add up to the targetSum
                        Returns (-1,-1) if no such pair exists

        Raises:
        ValueError : if the input list contain at least two elements to find a pair 
        """
        if len(arr) < 2:
            raise ValueError("Array must be atleast two elements to find a pair")
        start_pointer = 0
        end_pointer = len(arr) - 1
        while (start_pointer < end_pointer):
            temp_sum = arr[start_pointer] + arr[end_pointer]
            if temp_sum == targetSum :
                return (start_pointer,end_pointer)
            elif temp_sum < targetSum :
                start_pointer+=1
            else :
                end_pointer-=1
        return (-1,-1)