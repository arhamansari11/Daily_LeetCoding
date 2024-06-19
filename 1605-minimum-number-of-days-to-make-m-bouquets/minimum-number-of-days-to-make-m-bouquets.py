class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low < high:
            mid = ( low + high ) // 2
            flowers = 0
            bonq = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    flowers += 1
                    if flowers == k:
                        bonq += 1
                        flowers= 0
                else:
                    flowers = 0
                if bonq >= m:
                    break
            if bonq >= m:
                high = mid
            else:
                low = mid + 1

        return low
