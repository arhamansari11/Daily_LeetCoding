class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [-1]
        set_arr = set(arr)

        for i in set_arr:
            if arr.count(i) == i:
                count.append(i)
        
        maximum = max(count)

        return maximum

