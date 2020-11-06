# coding=utf-8
from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if d.get(v) is not None:
                return[d.get(v), i]
            d[target-v] = i



def test():
    sol = Solution()


if __name__ == '__main__':
    test()

