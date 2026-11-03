class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if str(num) in seen:
                return True
            seen[str(num)] = True
        return False