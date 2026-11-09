class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def num_of_hours(current_h: int) -> int:
            num_of_hours = 0
            for pile in piles:
                num_of_hours+= (pile + current_h - 1)// current_h
            return num_of_hours

        max_rate  = max(piles)
        left, right = 1, max_rate
        while left < right:
            mid = (left+right)//2
            #[fff tt ttt]
            if num_of_hours(mid) > h:
                left = mid +1
            else:
                right = mid
        return right


"""piles=[3,6,7,11]
# 3 6 7 11
# 0 1 1 2
# 3 2 3 3
3//6 = 0 6%3 =0

h=8

[1 6 11]"""
        





        