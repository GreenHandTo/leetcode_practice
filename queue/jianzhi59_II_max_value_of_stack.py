# 原题链接https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/
# idea：使用两个队列，一个存储值，一个存储最大值。
# 最大值队列是单调递减队列，使用一个双端队列来存储当前队列里的最大值，每向第一个队列里添加值时
# 会在单调递减队列里检查当前值是否大于递减队列里的队尾元素，如果大于会将元素从队尾pop出来直到
# 值不大于队尾元素或者队列为空，这样就维护了单调递减性，同时第一个队列在pop元素时，如果pop出来
# 的值和递减队列里的不一样，直接将值返回，否则将递减队列里的队首元素也pop出来，这样保证最大值的
# 一致性。（在向递减队列添加元素时，是比较的大于，所以等于队尾元素大小的值是直接添加到递减队列里的
# 所以不存在递减队列里pop出了和存储队列一样的元素，如果后面还有一样元素会有问题的问题）
from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.deque = deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        res = self.queue.popleft()
        if res == self.deque[0]:
            self.deque.popleft()
        return res