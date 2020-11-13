# coding=utf-8


class Solution(object):

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 1
        dic = {}

        for i, v in enumerate(s, 1):
            tmp = dic.get(v)
            if tmp and tmp >= start:
                max_len = max(max_len, i - start)
                start = tmp + 1
            dic[v] = i

        return max(max_len, len(s) + 1 - start)


def test():
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcdefgabcde'))
    print(sol.lengthOfLongestSubstring('abcdbaee'))
    print(sol.lengthOfLongestSubstring(' '))
    print(sol.lengthOfLongestSubstring('abba'))
    print(sol.lengthOfLongestSubstring('abcabcbb'))


if __name__ == '__main__':
    test()

