class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        if n < 2:
            return 0
        
        l, r, sum = 0, n - 1, 0
        lv, rv = h[l], h[r]

        while l < r:
            if h[l] < h[r]:
                l += 1
                while lv >= h[l] and l < r:
                    sum += lv - h[l]
                    l += 1
                lv = h[l]
            else:
                r -= 1
                while rv >= h[r] and l < r:
                    sum += rv - h[r]
                    r -= 1
                rv = h[r]
            

        return sum