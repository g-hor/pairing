# 852. Peak Index in a Mountain Array

# An array arr is a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # start searching at the halfpoint in arr
        # if the halfpoint is greater than elements to either side, then halfpoint is the peak
        # otherwise, search in the direction that goes up

        start = 0
        end = len(arr)
        peak = (end - start) // 2

        # while the current peak is not greater than either side of it, we know we have not found the peak yet
        while not (arr[peak] > arr[peak - 1] and arr[peak] > arr[peak + 1]):
            if arr[peak] < arr[peak - 1]:
                end = peak
                peak = (end - start) // 2
            else:
                start = peak # 4
                peak += (end - start) // 2

        return peak