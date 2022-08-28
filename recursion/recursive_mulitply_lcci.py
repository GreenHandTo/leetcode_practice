# https://leetcode.cn/problems/recursive-mulitply-lcci/
# 计算机乘法位运算是：
# 先计算被乘数的奇偶性，然后被乘数A右移一位得到a，乘数B左移一位b，结果为:
# 如果被乘数是偶数，为a*b
# 如果被乘数是奇数，为a*b+B
# 一直递归，直到其中一个数为0，则两数的积肯定是0的
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 0:
            return 0
        if A > B:
            A, B = B, A
        odd = False
        if A & 1 == 1:
            odd = True
        if not odd:
            return self.multiply(A>>1, B<<1)
        else:
            return self.multiply(A>>1, B<<1) + B