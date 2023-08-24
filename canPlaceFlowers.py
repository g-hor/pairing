# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # loop through the flowerbed list
        #   > if current space is 0
        #     > check of next space is also 0 OR if the current space is the last space
        #       > plant a flower by decrementing n
        #       > also increase space to two more spaces, which is the most nearby immediate space we can plant another flower
        #     > if not, we know the space is occupied by a plant
        #       > skip three spaces, which is two spaces away from the flower
        # returns boolean by checking if at least n plants have been planted

        flowerSpace = 0 

        while flowerSpace < len(flowerbed):
            if flowerbed[flowerSpace] == 0:
                if flowerSpace == len(flowerbed) - 1 or flowerbed[flowerSpace + 1] == 0:
                    n -= 1
                    flowerSpace += 2
                else: 
                    flowerSpace += 3
            else:
                flowerSpace += 2

        return n <= 0
                