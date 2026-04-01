class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        L, R = 0, len(string) - 1
        while L < R:
            if string[L] != string[R]:
                return False
            L += 1
            R -= 1
        return True