import collections
import numpy as np
from typing import List


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


#There's a sick recursive method should definitely check that out.

#96.97
#97.58
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return
        stack = [head]
        nextStack = []
        while len(stack) > 0:
            curr = stack.pop()
            if not curr: continue
            if curr.child:
                nextStack.append(curr.next)
                next = curr.child
                next.prev = curr
                curr.child = None
                curr.next = next
                stack.append(next)
            elif curr.next:
                stack.append(curr.next)
            elif not curr.next:
                if len(nextStack) > 0:
                    curr.next = nextStack[-1]
                    if curr.next:
                        curr.next.prev = curr
                    stack.append(nextStack.pop())
        return head

sll = Node(1, next=Node(2,
                        next = Node(3, child=Node(7, next= Node(8,
                                                                next = Node(9))),
                                    next=Node(4,
                                              next=Node(5,
                                                        next=Node(6,
                                                                  ))))))

s = Solution()
s.flatten(sll)
s.flatten(None)