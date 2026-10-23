class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for key, value in hashmap.items():
            buckets[value].append(key)

        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result

