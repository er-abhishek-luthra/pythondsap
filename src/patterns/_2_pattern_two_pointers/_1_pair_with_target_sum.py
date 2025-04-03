from typing import List, Tuple

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