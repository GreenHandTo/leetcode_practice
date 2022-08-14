class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递减栈，遍历所有的气温，
        #   1.如果栈为空，直接将当前气温代表的index加入栈
        #   2.如果栈不为空，栈顶元素代表的气温比当前气温高，则直接将气温代表的index加入栈
        #   3.如果栈不为空，栈顶元素代表的气温比当前气温低，则表示栈顶元素气温的日期到当前
        #     气温日期是增长的，计算差的天数即为栈顶元素气温的日期临近的最近几天后气温升高，
        #     并将栈顶元素pop出，继续拿新的栈顶元素对应的气温和当前气温对比，直到栈为空
        #     或者栈顶元素对应的气温不比当前气温小，将当前气温入栈
        stack = []
        result = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result