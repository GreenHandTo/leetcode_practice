# 使用快速幂算法，本质就是二分
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n < 0:
            x, n = 1/x, -n
        res = 1

        while n:
            if n & 1 == 1:
                res *= x
            # 注意这里 x*=x, x^2*=x^2,x^4*=x*4,x^8*=x^8
            x *= x
            n >>= 1
        return res