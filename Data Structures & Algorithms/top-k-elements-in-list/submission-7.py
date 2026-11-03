class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = [[] for i in range(len(nums) + 1)]
        for key, v in count.items():
            heap[v].append(key)
        ans = []
        for num in heap[::-1]:
            for a in num:
                if len(ans) < k:
                    ans.append(a)
        return ans