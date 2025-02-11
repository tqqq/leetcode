# coding=utf-8
"""
Question:
Difficulty: Easy
Detail:

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


"""


class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        nid = 0
        for i, c in enumerate(haystack):
            if i+ len(needle) > len(haystack):
                return -1
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1






    def sol2(self, haystack: str, needle: str) -> int:
        return haystack.index(needle)


if __name__ == "__main__":
    sol = Solution()
    # sol.run()

