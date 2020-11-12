# coding=utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        flag = 0

        while 1:
            tmp = l1.val + l2.val + flag
            l1.val = tmp % 10
            flag = tmp // 10

            if not l2.next:
                break
            if not l1.next:
                l1.next = l2.next
                break

            l1 = l1.next
            l2 = l2.next

        while flag and l1.next:
            l1 = l1.next
            tmp = l1.val + flag
            l1.val = tmp % 10
            flag = tmp // 10

        if flag:
            l1.next = ListNode(1, None)
        return head


def gen_list(array):
    head = ListNode(0, None)

    l1 = head

    for i in array:
        l1.next = ListNode(i, None)
        l1 = l1.next
    return head.next


def test():
    sol = Solution()
    l1 = gen_list([9, 3, 5, 6, 2])
    l2 = gen_list([4, 2, 1, 7, 7, 9])
    ans = sol.addTwoNumbers(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next





if __name__ == '__main__':
    test()

