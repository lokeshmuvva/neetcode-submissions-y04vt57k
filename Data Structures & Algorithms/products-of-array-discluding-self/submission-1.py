class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        suffix = []
    
        total = 1
        for num in nums:
            prefix.append(total)
            total *= num

        total = 1
        for num in reversed(nums):
            suffix.append(total)
            total *= num

        suffix.reverse()

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output
            