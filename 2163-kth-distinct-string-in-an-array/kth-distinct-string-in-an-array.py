class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = [""]

        for i in arr:
            if arr.count(i) == 1:
                res.append(i)

        if len(res) <= k:
            return ""
        else:
            return res[k]