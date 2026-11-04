class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        needed = {}
        j = len(numbers) - 1
        for i, first in enumerate(numbers):
            needed = target - first

            while j > i and numbers[j] > needed:
                j -= 1
            if needed == numbers[j]:
                return [i + 1, j + 1]
