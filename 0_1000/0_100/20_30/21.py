# coding=utf-8
"""
Question:
Difficulty: Easy
Detail:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head1 = list1
        head2 = list2
        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        cur = head
        while True:
            if not head1:
                cur.next = head2
                return head
            if not head2:
                cur.next = head1
                return head
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next



if __name__ == "__main__":
    sol = Solution()
    # sol.run()

