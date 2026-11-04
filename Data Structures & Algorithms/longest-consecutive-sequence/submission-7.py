class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = defaultdict(int)
        res = 0

        for num in nums:
            if not mem[num]:
                mem[num] = mem[num - 1] + mem[num + 1] + 1
                mem[num - mem[num - 1]] = mem[num]
                mem[num + mem[num + 1]] = mem[num]
                res = max(res, mem[num])
        return res
