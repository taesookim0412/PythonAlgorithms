from _collections import OrderedDict


#Runtime: 176 ms, faster than 95.19% of Python3 online submissions for LRU Cache.
#Memory Usage: 23.4 MB, less than 6.06% of Python3 online submissions for LRU Cache.
#godbless ordered hashmaps

class LRUCache:

    data = OrderedDict()
    max = 0
    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.max = capacity
    def get(self, key: int) -> int:
        if key not in self.data: return -1
        val = self.data[key]
        del self.data[key]
        self.data[key] = val
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            del self.data[key]
            self.data[key] = value
        else:
            if len(self.data) < self.max:
                self.data[key] = value
            else:
                delkey = next(iter(self.data))
                del self.data[delkey]
                self.data[key] = value





















#possible to attempt with OrderedDict however
#want indexing practice

#11 / 18 test cases passed.
#doesnt update the indexes
#a possiblity is a high fixed array of index = key
#requires a DLL

# class LRUCache:
#     data = {}
#     order = []
#     max = 0
#     def __init__(self, capacity: int):
#         self.reset(capacity)
#     def get(self, key: int) -> int:
#         if key not in self.data: return -1
#         self.pushToEnd(key)
#         print(self.order)
#         return self.data[key][1]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.data:
#             self.data[key] = [self.data[key][0], value]
#             self.pushToEnd(key)
#         else:
#             if len(self.data) < self.max:
#                 self.order.append(key)
#                 self.data[key] = [len(self.order)-1, value]
#             else:
#                 #delete and insert
#                 keyToDelete = self.order[0]
#                 del self.data[keyToDelete]
#                 del self.order[0]
#                 self.order.append(key)
#                 self.data[key] = [len(self.order)-1, value]
#         #print(cache.data)
#
#
#
#     def reset(self, capacity):
#         self.data = {}
#         self.order = []
#         self.max = capacity
#
#     def pushToEnd(self, key):
#         idxOfKey = self.data[key][0]
#         del self.order[idxOfKey]
#         self.order.append(key)
#         self.data[key][0] = len(self.order)-1



cache = LRUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print()#evicts key 2)
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
print(cache.get(5))
print(cache.data)
print(cache.put(5, 5))
print(cache.data)
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# class LRUCache:
#     data = {}
#     max = 0
#     counter = 0
#     insertions = []
#     indexes = {}
#
#     def __init__(self, capacity: int):
#         self.reset()
#         self.max = capacity
#     def get(self, key: int) -> int:
#         #get key's index in insertion
#         #move it to the end
#         if key not in self.data: return -1
#         idx = self.indexes[key]
#
#         keyToSwap = self.insertions[0]
#         #doubleswap
#         self.insertions[idx], self.insertions[0] = self.insertions[0], self.insertions[idx]
#         #swap index
#         self.indexes[key], self.indexes[keyToSwap] = self.indexes[keyToSwap], self.indexes[key]
#         return self.data[key]
#     def put(self, key: int, value: int) -> None:
#         insert = False if key in self.data else True
#         self.data[key] = value
#         if insert:
#             self.insertions.append(key)
#             self.indexes[key] = len(self.insertions)-1
#         if len(self.insertions) > self.max:
#             key = self.insertions[0]
#             del self.indexes[key]
#             del self.data[key]
#         print(F"Data: {self.data}, Insertions: {self.insertions}, Indexes: {self.indexes}")
#     #required for lc
#     def reset(self):
#         self.data = {}
#         self.max = 0
#         self.counter = 0
#         self.insertions = []
#         self.indexes = {}