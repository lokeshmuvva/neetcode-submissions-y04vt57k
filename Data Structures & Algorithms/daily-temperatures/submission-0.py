class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for temperature in temperatures]
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                popped = stack.pop()
                output[popped[1]] = (index - popped[1])
            stack.append((temperature, index)) 
        return output