class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(0, len(nums) + 1)]
        freqMap = {num: 0 for num in nums}
        for num in nums:
            freqMap[num] += 1
        for num, count in freqMap.items():
            buckets[count].append(num)
        
        result = []
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result