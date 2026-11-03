class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        for n in nums:
            res.append(prod)
            prod *= n
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = prod * res[i]
            prod *= nums[i]
        return res