class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        start = 0
        max_len = 0
        for i, value in enumerate(s):
            count[value] += 1
            length = i-start+ 1
            if k < length - max(count.values()):
                count[s[start]] -= 1
                start += 1
                length -= 1
            max_len = max(length, max_len)
        return max_len

        