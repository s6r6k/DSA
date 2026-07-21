class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #top k frequent needs a max heap. the heap will contain lists, ele 1 of the list will be the count and 
        dict = {}
        for val in nums:
            if val in dict:
                dict[val] += 1
            else:
                dict[val] = 1
        heap = []
        for key, val in dict.items():
            list = [(-1 * val), key]
            heapq.heappush(heap, list)
        result = []
        for i in range(k):
            listi = heapq.heappop(heap)
            result.append(listi[1])
        return result

        