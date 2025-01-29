class Solution:
    def secondHighest(self, s: str) -> int:
        arr = []
        for i in s:
            if i.isdigit():
                if int(i) not in arr:
                    arr.append(int(i))
        
        arr.sort()
        length = len(arr)
        if length >= 2:
            return arr[length-2]

        return -1