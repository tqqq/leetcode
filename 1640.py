# coding=utf-8


class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        flag = 0

        for i in self.gen(pieces):
            flag ^= i
        for i in arr:
            flag ^= i

        if flag:
            return False

        pieces.sort(key=(lambda x: arr.index(x[0])))

        for i, v in enumerate(self.gen(pieces)):
            if arr[i] != v:
                return False

        return True

    def gen(self, a):
        for arr in a:
            for i in arr:
                yield i


def test():
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6]
    pieces = [[3], [6], [4, 5], [1, 2]]

    ans = sol.canFormArray(arr=arr, pieces=pieces)
    print(str(ans))


if __name__ == '__main__':
    test()

