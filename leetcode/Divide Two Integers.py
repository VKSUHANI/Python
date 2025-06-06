class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math
        if (dividend > 0 and divisor > 0):
            r=math.floor(dividend/divisor)
            return r
        else:
            dividend=abs(dividend)
            divisor=abs(divisor)
            r=math.floor(dividend/divisor)
            return -r
            


dividend = 7
divisor = -3
Solution= Solution()
result = Solution.divide(dividend, divisor)
print(result)  # Output: 0