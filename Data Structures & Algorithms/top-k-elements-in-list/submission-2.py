class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = []
        for (key, v) in count.items():
            heapq.heappush(heap, (v, key))

            if (len(heap) > k):
                heapq.heappop(heap)
        
        return [a[1] for a in heap]