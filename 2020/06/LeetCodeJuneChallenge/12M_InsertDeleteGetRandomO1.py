class RandomizedSet:
#58% Faster
#73% Less Memory
#https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/683168/Python-58-Faster-73-Less-Memory-Dict-%2B-List
#"Basically never pops elements out of the spare list and loops random indexes inside of the list until the dictionary contains the key."
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.dataList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        data = self.data
        dataList = self.dataList
        if val in data: return False
        data[val] = val
        dataList.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        data = self.data
        if val not in data:
            return False
        del data[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand = random.randrange(len(self.dataList))
        while (self.dataList[rand] not in self.data):
            rand = random.randrange(len(self.dataList))
        return self.dataList[rand]