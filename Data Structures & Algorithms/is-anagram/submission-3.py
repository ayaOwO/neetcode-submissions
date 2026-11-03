class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        seen = defaultdict(lambda: 0)
        for char in s:
            seen[char] += 1
        seenSecond = defaultdict(lambda: 0)
        for char in t:
            seenSecond[char] += 1
            if seenSecond[char] > seen[char]:
                return False
                
        return True
        