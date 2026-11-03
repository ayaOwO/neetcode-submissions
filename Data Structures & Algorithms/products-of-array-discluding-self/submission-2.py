class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = [1]
        for n in nums:
            res.append(res[-1] *n)
        
        res.pop()
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = prod * res[i]
            prod *= nums[i]
        return res