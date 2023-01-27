'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21'''

class Solution:
    def reverse(self, x: int) -> int:
        def cal(x:int):
            x = str(x)
            if x[0]=='-':
                k= x[1:(len(x)+1)]
                return 0-int(k[::-1])
            else:
                return int(x[::-1])


        def cond(x:int):
            return (x>-2**31) and x<(2**31)-1
        if cond(x):
            c =cal(x)
            if cond(c):
                return c
            else:
                return 0
        else:
            return 0