class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            if tuple(sorted(i)) in hashmap:
                hashmap[tuple(sorted(i))].append(i)
            else:
                hashmap[tuple(sorted(i))] = [i]
        
        return list(hashmap.values())

        