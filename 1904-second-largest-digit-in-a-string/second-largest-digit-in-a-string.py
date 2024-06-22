class Solution:
    def secondHighest(self, s: str) -> int:
        arr = []
        for i in s:
            if i.isdigit():
                arr.append(int(i))
        
        set1 = set(arr)
        list1 = list(set1)
        list1.sort()
        if len(list1) >= 2:
            return list1[-2]
        
        return -1

