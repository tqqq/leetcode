# coding=utf-8


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if not nums1:
            if not nums2:
                return None
            if len(nums2) == 1:
                return nums2[0]
            else:
                return self.findMedianSortedArrays(nums2[:1], nums2[1:])
        if not nums2:
            return self.findMedianSortedArrays(nums2, nums1)

        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.find_kth_number(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, length//2) +
                    self.find_kth_number(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, length//2+1)) / 2
        else:
            return self.find_kth_number(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, (length+1)//2)

    def find_kth_number(self, nums1, nums2, start_1, end_1, start_2, end_2, k):
        len_1 = end_1 - start_1 + 1
        len_2 = end_2 - start_2 + 1

        if len_2 == 1:
            if k > len_1:
                return max(nums1[end_1], nums2[start_2])
            if k == 1:
                return min(nums1[start_1], nums2[start_2])
            return self.get_mid(nums1[start_1 + k - 2],
                                nums1[start_1 + k - 1], nums2[start_2])
        if len_1 == 1:
            return self.find_kth_number(nums2, nums1, start_2, end_2, start_1, end_1, k)

        cursor_1 = start_1 + (len_1 * k - 1)//(len_1 + len_2)
        cursor_2 = start_2 + (len_2 * k - 1)//(len_1 + len_2)

        if nums1[cursor_1] > nums2[cursor_2]:
            return self.find_kth_number(nums1, nums2, start_1, cursor_1,
                                        cursor_2, end_2, k - cursor_2 + start_2)
        else:
            return self.find_kth_number(nums1, nums2, cursor_1, end_1,
                                        start_2, cursor_2, k - cursor_1 + start_1)

    def get_mid(self, a, b, c):
        if a > b:
            if b > c:
                return b
            else:
                return min(a, c)
        else:
            if a > c:
                return a
            else:
                return min(b, c)


def test():
    sol = Solution()
    n1 = [2, 3]
    n2 = [1, 4]

    c = sol.findMedianSortedArrays(n1, n2)
    print(c)


if __name__ == '__main__':
    test()

