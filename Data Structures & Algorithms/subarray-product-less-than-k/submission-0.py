class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        L = 0
        total = 1
        count = 0
        for R in range(len(nums)):
            total *= nums[R]
            while total >= k:
                total //= nums[L]
                L += 1
            count += (R - L + 1)
        return count