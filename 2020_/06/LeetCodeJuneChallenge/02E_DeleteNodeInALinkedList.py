#83% faster runtime
#06-02-2020_

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        runner = node
        while runner.next:
            runner.val = runner.next.val
            if runner.next.next == None:
                runner.next = None
            if runner.next == None:
                return
            runner = runner.next