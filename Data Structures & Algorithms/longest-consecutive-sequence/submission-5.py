class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sliding window
        if nums == []:
            return 0
        ordered = sorted(nums)
        last = ordered[0]
        first = last
        length = 0
        for n in ordered[1:]:
            if n not in (last + 1, last):
                dist = abs(last - first) + 1
                length = max(length, dist)
                first = n
            last = n
        dist = abs(last - first) + 1
        length = max(length, dist)

        return length
