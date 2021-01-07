class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = list(reversed(sorted(boxTypes, key=lambda x: x[1])))
        boxes = 0
        units = 0
        for i in range(len(boxTypes)):
            for j in range(boxTypes[i][0]):
                if boxes + 1 > truckSize:
                    break
                units += boxTypes[i][1]
                boxes += 1
        return units
