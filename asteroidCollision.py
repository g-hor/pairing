# 735. Asteroid Collision

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create List to hold asteroids that do not collide
        # loop over asteroids input list:
        #   > if the current num and next num are not pos -> neg pair
        #   > then append current num to holder List
        #   >> otherwise, compare pos -> neg pair to determine outcome of collision
        #   >> then compare the winner to the last appended item to holder List
        # [2,3,5,6,7,87,89,32,-100]

        winners = []
        idx = 0
        
        while idx < len(asteroids) - 1:
            # 2
            current = asteroids[idx] # -2
            next = asteroids[idx + 1] # -2
            # [-2, -2]

            if (current > 0) and (next < 0):
                # collision condition logic:
                if (current + next) > 0:
                    winners.append(current)
                elif (current + next) < 0:
                    while winners:
                        last = winners[-1] # -2
                        next = asteroids[idx + 1] # -2

                        if last > 0:
                            if (last + next) < 0:
                                winners.pop()
                            elif (last + next) > 0:
                                idx += 1
                                break
                            elif (last + next) == 0:
                                winners.pop()
                                idx += 1
                                break
                        else:
                            if idx == len(asteroids) - 2:
                                winners.append(next)
                            break
                elif (current + next) == 0:
                    idx += 1
            else:
                winners.append(current)
                if idx == len(asteroids) - 2:
                    winners.append(next)


            idx += 1


        return winners