class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        sortmap = sorted(hashmap.items(), 
                         key=lambda x: x[1],
                         reverse=True)

        top_k = sortmap[:k]

        for i in top_k:
            result.append(i[0])

        return result
