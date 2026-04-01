class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for num in nums:
            if num not in duplicates:
                duplicates[num] = 1
            else:
                duplicates[num] += 1
        for i in duplicates:
            if duplicates[i] > 1:
                return True
        return False