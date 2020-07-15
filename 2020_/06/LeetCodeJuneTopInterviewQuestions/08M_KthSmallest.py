#Runtime: 44 ms, faster than 96.69% of Python3 online submissions for Kth Smallest Element in a BST.
#Memory Usage: 17.8 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.

class Solution:
    # Assume its ordered#
    # But how about the stack method?
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stax = []
        curr = root
        while curr or len(stax) > 0:
            while (curr):
                stax.append(curr)
                curr = curr.left
            curr = stax.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


#Heap Method
#Runtime: 44 ms, faster than 96.69% of Python3 online submissions for Kth Smallest Element in a BST.
#Memory Usage: 17.8 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        heap = []
        self.traverseInOrder(root, heap)
        return heapq.nsmallest(k, heap)

    def traverseInOrder(self, root, heap):
        if root:
            self.traverseInOrder(root.left, heap)
            heapq.heappush(heap, root.val)
            self.traverseInOrder(root.right, heap)