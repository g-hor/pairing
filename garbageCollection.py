# 2391. Minimum Amount of Time to Collect Garbage

# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

# There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

# Return the minimum number of minutes needed to pick up all the garbage.



class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # create counter variable to keep track of total amount of garbage
        # create last index variables to keep track of last index of appearance for each type of garbage
        # iterate through garbage list
        #   > check if garbage contains any type
        #   > increment counter by garbage amount
        #   > update last index variables to current index
        #  if counter is not zero
        #   > calculate travel time based on "last index" respective variable
        #  return travel time + amount of garbage


        amount = 0

        glassIdx = None
        metalIdx = None
        paperIdx = None

        for idx, trash in enumerate(garbage):
            if "G" in trash:
                glassIdx = idx
            if "M" in trash:
                metalIdx = idx
            if "P" in trash:
                paperIdx = idx

            amount += len(trash)

        if glassIdx:
            for time in range(glassIdx):
                amount += travel[time]
        if metalIdx:
            for time in range(metalIdx):
                amount += travel[time]
        if paperIdx:
            for time in range(paperIdx):
                amount += travel[time]

        return amount