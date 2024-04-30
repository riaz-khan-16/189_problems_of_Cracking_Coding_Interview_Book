#https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
def findKthLargest( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxheap=[-i for i in nums]
        heapq.heapify(maxheap)
        for x in range(k-1):
            heapq.heappop(maxheap)
        answer=heapq.heappop(maxheap)
        return -answer 