class Solution:
    def candy(self, ratings: List[int]) -> int:
        s = 1
        n = len(ratings)
        i = 1
        while i < n:
            if ratings[i] == ratings[i-1]:
                s += 1
                i += 1
                continue
            peek = 1
            while i < n and ratings[i] > ratings[i -1]:
                peek += 1
                s += peek
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                s += down
                down += 1
                i += 1
            if down > peek:
                s += down - peek
        return s