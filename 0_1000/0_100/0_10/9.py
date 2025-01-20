# coding=utf-8
"""
Question:
Difficulty: Easy
Detail:




"""


class Solution(object):
    """
    Given an integer x, return true if x is a palindrome , and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        return str(x) == str(x)[::-1]

    def sol2(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False
        return True

    def sol3(self, x: int) -> bool:
        if x < 0:
            return False
        nums = []
        while x:
            nums.append(x % 10)
            x //= 10
        return nums == nums[::-1]



if __name__ == "__main__":
    s = Solution()
    # s.run()

