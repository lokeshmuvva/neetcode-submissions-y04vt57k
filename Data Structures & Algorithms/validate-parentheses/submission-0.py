class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if matching[char] != popped:
                    return False
        return not stack