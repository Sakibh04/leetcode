class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        l, r = 0, len(string_x) - 1
        while l < r:
            if string_x[l] != string_x[r]:
                return False
            else:
                l += 1
                r -= 1

        return True