class Solution:
    def trap(self, height: List[int]) -> int:
        # 本题还可以使用双指针，动态规划的解法
        # 基于单调栈的算法，时间复杂度O(n)，因为每个index只会入栈和出栈一次，空间复杂度O(n)
        # 单调递减栈，如果栈里没有元素或者当前高度比栈顶元素对应的高度小
        # 直接将高度对应的index入栈；
        # 如果有元素，并且当前高度比栈顶元素对应的高度大，那么开始计算这块面积：在栈里，栈顶元素
        # 下面的元素到当前index之间的大小为面积的长i-left-i,下面的元素和当前index
        # 对应的高度的最小值减去栈顶元素的值，为面积的宽度，最后乘起来得到这块的面积
        stack = []
        area = 0

        for i, v in enumerate(height):
            while stack and height[stack[-1]] < v:
                peek = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                long = i - left - 1
                width = min(height[left], v) - height[peek]
                area += long * width

            stack.append(i)
        return area