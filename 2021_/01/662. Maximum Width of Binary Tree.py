from collections import *

class Solution:
    def widthOfBinaryTree(self, root):
        q = deque()
        q.append([root, 1])
        maxWidth = 1
        while (len(q)):
            firstNode = q[0]
            startingSize = firstNode[1]
            sz = len(q)
            endSize = -1
            for i in range(sz):
                colNode = q.popleft()
                endSize = max(endSize, colNode[1])
                if colNode[0].left:
                    q.append([colNode[0].left, colNode[1] * 2])
                if colNode[0].right:
                    q.append([colNode[0].right, colNode[1] * 2 + 1])
            maxWidth = max(maxWidth, endSize - startingSize + 1)
        return maxWidth


#68ms
# import queue
#
#
# class Solution:
#     def widthOfBinaryTree(self, root):
#         q = queue.Queue()
#         q.put([root, 1])
#         maxWidth = 1
#         while (q.qsize() > 0):
#             firstNode = list(q.queue[0])
#             startingSize = firstNode[1]
#             sz = q.qsize()
#             endSize = -1
#             for i in range(sz):
#                 colNode = q.get()
#                 endSize = max(endSize, colNode[1])
#                 if colNode[0].left:
#                     q.put([colNode[0].left, colNode[1] * 2])
#                 if colNode[0].right:
#                     q.put([colNode[0].right, colNode[1] * 2 + 1])
#             maxWidth = max(maxWidth, endSize - startingSize + 1)
#         return maxWidth

##Original answer did not account for "Entire Width Span", instead I came up with two variants of:
#class Solution:
    # def widthOfBinaryTree(self, root):
    #     res_dict = collections.defaultdict(int)
    #     self.traverse(root, 0, res_dict)
    #     return res_dict[max(res_dict, key=lambda key: res_dict[key])]
    # def traverse(self, root, row, res_dict):
    #     if root:
    #         res_dict[row] += 1
    #         if root.left:
    #             self.traverse(root.left, row + 1, res_dict)
    #         if root.right:
    #             self.traverse(root.right, row + 1, res_dict)

#class Solution:
    # def widthOfBinaryTree(self, root):
    #     widths = collections.defaultdict(int)
    #     q = queue.Queue()
    #     maxWidth = 1
    #     currNode = [0, root]
    #     curr = root
    #     while curr:
    #         widths[currNode[0]] += 1
    #         row = currNode[0]
    #         maxWidth = max(maxWidth, widths[currNode[0]])
    #         if curr.left:
    #             q.put([row + 1, curr.left])
    #         if curr.right:
    #             q.put([row + 1, curr.right])
    #         nextNode = q.get()
    #         if not nextNode:
    #             break
    #         currNode = q.get()
    #     return maxWidth
    #
