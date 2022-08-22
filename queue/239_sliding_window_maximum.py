# 原题链接：https://leetcode.cn/problems/sliding-window-maximum/
# 还可以使用优先队列（即大顶/小顶堆）来实现，后面到堆的时候再实现一下
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotony_queue = deque()
        ret = []

        length = len(nums)
        for i in range(k):
            while monotony_queue and nums[monotony_queue[-1]] < nums[i]:
                monotony_queue.pop()
            monotony_queue.append(i)
        ret.append(nums[monotony_queue[0]])

        for i in range(k, length):
            while monotony_queue and monotony_queue[0] <= i-k:
                monotony_queue.popleft()
            while monotony_queue and nums[monotony_queue[-1]] < nums[i]:
                monotony_queue.pop()
            monotony_queue.append(i)
            ret.append(nums[monotony_queue[0]])
        return ret