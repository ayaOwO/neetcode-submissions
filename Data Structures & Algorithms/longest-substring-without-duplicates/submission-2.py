class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        m = 0
        dup = {}
        for i, char in enumerate(s):
            if char in dup and dup[char] >= start:
                start = dup[char] + 1
            dup[char] = i
            
            m = max(i-start + 1 , m)
        return m