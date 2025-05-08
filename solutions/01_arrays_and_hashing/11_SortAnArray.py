"""
Difficulty: [Medium]
NeetCode #: [11/250]
Date Solved: [03/05/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Use a sorting algorithm. Any would do as long as its time complexity is O(n log n).

Time Complexity: O(n log n)
Space Complexity: O(n)

Key Insights:
- Break the code into parts where mergeSort function handles left and right array 
while merge function handle combining both parts recusively.
"""

class Solution:
    def sortArray(self, nums):
        def merge(arr, L, M, R):
            left, right = arr[L : M + 1], arr[M + 1 : R + 1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return
        mergeSort(nums, 0, len(nums) - 1)
        return nums