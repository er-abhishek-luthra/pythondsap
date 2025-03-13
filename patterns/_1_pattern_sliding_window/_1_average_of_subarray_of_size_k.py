from typing import List

def find_averages(K: int, arr: List[int]) -> List[float]:
    result = [0.0] * (len(arr) - K + 1)
    window_sum = 0.0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'K'
        if window_end >= K - 1:
            result[window_start] = window_sum / K  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result

# Example usage
if __name__ == "__main__":
    result = find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K:", result)