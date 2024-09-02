class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        arr = []
        for i in bank:
            if "1" in i:
                arr.append(i)

        for i in range(len(arr)-1):
            count += arr[i].count('1')  *  arr[i+1].count('1')

        return count
