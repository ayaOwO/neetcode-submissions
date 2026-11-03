class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prods = [1]
        for n in nums[::-1]:
            prods.append(n * prods[-1])
        for i,n in enumerate(nums):
            nums[i] = prod * prods[-1 * (i+2)]
            prod *= n
        return nums


