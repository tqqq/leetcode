# coding=utf-8


class Solution(object):
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False
            x *= -1
        ans = 0
        while x != 0:
            ans *= 10
            ans += x % 10
            x = x // 10

        if flag:
            return ans if ans <= 2**31 else 0
        else:
            return ans*(-1) if ans < 2**31 else 0



def test():
    sol = Solution()
    pls = [
        123,
        1230,
        -123,
        -1230,
        2**31 - 1,
        2**31,
        -(2**31)
    ]
    for pl in pls:
        print(sol.reverse(pl))


if __name__ == '__main__':
    test()

