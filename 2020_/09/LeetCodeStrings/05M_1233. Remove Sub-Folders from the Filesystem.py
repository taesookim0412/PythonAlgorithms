import collections
import numpy as np
from typing import List


# class TrieNode():
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)


# ["/a","/a/b","/c/d","/c/d/e","/c/f"
# a in ab, cd in cde

# Runtime: 472 ms, faster than 25.59% of Python3 online submissions for Remove Sub-Folders from the Filesystem.
# Memory Usage: 50 MB, less than 8.73% of Python3 online submissions for Remove Sub-Folders from the Filesystem.

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        dirs = set()
        folders = sorted(list(filter(None,folder.split('/'))) for folder in folders)
        for folder_fp in folders:
            curr_name = ""
            for folder in folder_fp:
                curr_name += f"/{folder}"
                if curr_name in dirs:
                    break
            else:
                dirs.add(curr_name)
        return dirs


s = Solution()
print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(s.removeSubfolders(["/ah/al/am","/ah/al"]))