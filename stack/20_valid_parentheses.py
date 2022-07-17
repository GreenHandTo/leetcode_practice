class Solution:
    def isValid(self, s: str) -> bool:
        # 先判断是否是偶数
        if len(s) & 1 == 1:
            return False
        
        # 将左括号按顺序放到栈中，遇到右括号，判断栈顶元素与右括号是否匹配，
        # 否直接返回False，是的话pop掉栈顶元素，直到最后如果栈中还有元素的话，返回False
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                # 右括号先出现，但是栈是空的或者栈顶是元素和右括号不匹配
                if not stack or pairs[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()

        return not stack
