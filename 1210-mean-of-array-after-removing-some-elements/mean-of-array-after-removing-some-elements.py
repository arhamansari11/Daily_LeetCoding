class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        percent = 5
        per = (percent / 100) * n
        ro = round(per)
        new = arr[ro : n - ro]
        n1 = len(new)
        add= sum(new) / n1
        return add