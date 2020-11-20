# coding=utf-8


class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        ans = ''
        tmp = 0
        unit = 2*numRows-2
        while tmp < len(s):
            ans = ans + s[tmp]
            tmp += unit
        for i in range(1, numRows - 1):
            tmp1 = i
            tmp2 = unit - i
            while tmp2 < len(s):
                ans += s[tmp1]
                ans += s[tmp2]
                tmp1 += unit
                tmp2 += unit
            if tmp1 < len(s):
                ans += s[tmp1]

        tmp = numRows - 1
        while tmp < len(s):
            ans += s[tmp]
            tmp += unit

        return ans









def test():
    sol = Solution()
    print(sol.convert('abcdcbabcdcbabcdcbabc', 4))




if __name__ == '__main__':
    test()

