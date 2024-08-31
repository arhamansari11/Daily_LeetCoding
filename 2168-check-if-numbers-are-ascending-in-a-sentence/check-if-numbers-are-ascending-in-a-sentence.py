class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        x = s.split()
        arr = []
        for i in x:
            if i.isnumeric():
                arr.append(int(i))

        boolean = True
        if len(arr) > 1:
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    boolean = False
                    break

        return boolean