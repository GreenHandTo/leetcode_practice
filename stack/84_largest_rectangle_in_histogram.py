# 1.单调递增栈，未优化算法，时间复杂度O(N)，空间复杂度O(N)
# 详见https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
class SolutionOne:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        length = len(heights)

        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                while stack and heights[stack[-1]] == cur_height:
                    stack.pop()
                if stack:
                    # 注意这里的计算，因为有可能最后一个被pop掉的元素，在他初始入栈前可能栈里面是有比他
                    # 对应的高度大的元素的，只不过要计算他对应的最大面积所以被pop掉了，所以这里计算宽度
                    # 时，是根据栈最后一个元素来计算，他们i～stack[-1]之间的元素对应的高度肯定是>=cur
                    # 对应的高度的
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = max(area, width * cur_height)
            stack.append(i)

        while stack:
            cur_height = heights[stack.pop()]
            while stack and heights[stack[-1]] == cur_height:
                stack.pop()
            if stack:
                # 注意这里的宽度计算，剩下的元素对应的高度在栈里是单调递增的，宽度要从整个heights的长度
                # 开始计算，栈里面最后一个元素到heights的最后一个index之间的高度肯定是比栈顶元素对应的
                # 高度大或者相等(heights的最后一个index与栈顶元素相等时是相等的)
                width = length - stack[-1] - 1
            else:
                width = length
            area = max(area, width * cur_height)
        return area


# 2.优化过的单调递增栈,时间复杂度O(N)，空间复杂度O(N)
class SolutionTwo:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        area = 0
        length = len(heights)

        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                while stack and heights[stack[-1]] == cur_height:
                    stack.pop()
                if stack:
                    # 注意这里的计算，因为有可能最后一个被pop掉的元素，在他初始入栈前可能栈里面是有比他
                    # 对应的高度大的元素的，只不过要计算他对应的最大面积所以被pop掉了，所以这里计算宽度
                    # 时，是根据栈最后一个元素来计算，他们i～stack[-1]之间的元素对应的高度肯定是>=cur
                    # 对应的高度的
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = max(area, width * cur_height)
            stack.append(i)
        return area