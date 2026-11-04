class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        low = s.lower()
        j = len(s) - 1
        while j > i:
            while not (low[j].isalpha() or low[j].isdigit()):
                j -= 1
                if i >= j:
                    return True
            while not (low[i].isalpha() or low[i].isdigit()):
                i += 1
                if i >= j:
                    return True
            if low[i] != low[j]:
                return False

            i += 1
            j -= 1
        return True
