from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, head) -> None:
        while head is not None:
            print(head.val)
            head = head.next
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        # Reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge two lists
        second = prev
        first = head
        while second:
            temp_first = first.next
            temp_second = second.next
            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second

sol = Solution()
sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
