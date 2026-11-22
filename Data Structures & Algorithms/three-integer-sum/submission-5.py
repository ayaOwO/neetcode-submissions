class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            target = -val
            start = i + 1
            end = len(nums) - 1
            while start < end:
                match nums[start] + nums[end]:
                    case total if total > target:
                        end -= 1
                    case total if total < target:
                        start += 1
                    case target:
                        triplets.append((nums[start], nums[end], val))
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1

        return triplets
