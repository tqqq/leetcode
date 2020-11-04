# coding=utf-8


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, v in enumerate(nums[1:], 1):
            nums[i] += nums[i - 1]
        return nums


def test():
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    answer = sol.runningSum(nums=nums)
    print(str(answer))


if __name__ == '__main__':
    test()
