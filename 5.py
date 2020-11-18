# coding=utf-8


class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s
        pal = s[0]
        for i in range(0, length - 1):
            if s[i] == s[i+1]:
                left = i
                right = i + 1
                while left >= 0 and right <= length-1 and s[left] == s[right]:
                    left -= 1
                    right += 1
                if len(pal) < right - left - 1:
                    pal = s[left+1:right]
            left = i
            right = i
            while left >= 0 and right <= length - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            if len(pal) < right - left - 1:
                pal = s[left + 1:right]
        return pal


def test():
    sol = Solution()
    payloads = [
        'abcdedcba',
        'safdfsadfg',
        'abbc',
        'abcabc',
        'cbbd',
        'bb'
    ]

    for p in payloads:
        print(sol.longestPalindrome(p))


if __name__ == '__main__':
    test()

