# coding=utf-8


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        a = max(candies) - extraCandies

        return [c >= a for c in candies]


def test():
    sol = Solution()
    ans = sol.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3)
    print(ans)


if __name__ == '__main__':
    test()

