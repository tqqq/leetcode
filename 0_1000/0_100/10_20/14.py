# coding=utf-8
"""
Question:
Difficulty: Easy
Detail:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.



"""

from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if len(strs) == 1 or strs[0] == "":
            return strs[0]
        common = ""
        while True:
            if i > len(strs[0]):
                return common
            for s in strs[1:]:
                if i > len(s):
                    return s
                if s[:i] != common:
                    return strs[0][:i-1]
            i += 1
            common = strs[0][:i]




if __name__ == "__main__":
    s = Solution()
    # s.run()

