#Runtime: 44 ms, faster than 73.53% of Python3 online submissions for Odd Even Linked List.
#Memory Usage: 15.8 MB, less than 24.99% of Python3 online submissions for Odd Even Linked List.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #inplace
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return head
        odd = head
        even = head.next
        evenHead = head.next
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head



sol = Solution()
nd = ListNode(1)
nd.next = ListNode(2)
nd.next.next = ListNode(3)
nd.next.next.next = ListNode(4)
nd.next.next.next.next = ListNode(5)
print(sol.oddEvenList(nd))

