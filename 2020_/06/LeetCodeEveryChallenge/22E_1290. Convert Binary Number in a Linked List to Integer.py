#Runtime: 20 ms, faster than 98.66% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
#Memory Usage: 13.9 MB, less than 27.50% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        curr = head
        while curr:
            nums += curr.val,
            curr = curr.next
        num = 0
        for i in range(len(nums)-1, -1, -1):
            num += nums[i] * 2**(len(nums)-1-i)
        return num

#Runtime: 32 ms, faster than 53.59% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
#Memory Usage: 14.1 MB, less than 5.38% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        curr = head
        while curr:
            nums += curr.val,
            curr = curr.next
        num = ''.join([str(x) for x in nums])
        return int(num, 2)


s = Solution()
sll = ListNode(1)
sll.next = ListNode(0)
sll.next.next = ListNode(0)
sll.next.next.next = ListNode(1)

print(s.getDecimalValue(sll))
#[1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
#18880