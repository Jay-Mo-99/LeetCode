class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        up = 1
        down1 = 1
        down2=1
        

        for i in range(1,m+n-1):
            up *= i
        for i in range(1,m):
            down1 *= i
        for i in range(1,n):
            down2 *= i

        return int(up/(down1*down2))