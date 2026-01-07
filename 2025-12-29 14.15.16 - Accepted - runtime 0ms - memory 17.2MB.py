class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # For each element, count how many odd-length subarrays include it
        # Element at index i appears in subarrays starting at [0..i] and ending at [i..n-1]
        # Number of subarrays containing arr[i] = (i+1) * (n-i)
        # Half of them (rounded up) have odd length
        # Time: O(n), Space: O(1)
        n = len(arr)
        result = 0
        for i, val in enumerate(arr):
            total_subarrays = (i + 1) * (n - i)
            odd_subarrays = (total_subarrays + 1) // 2
            result += val * odd_subarrays
        return result