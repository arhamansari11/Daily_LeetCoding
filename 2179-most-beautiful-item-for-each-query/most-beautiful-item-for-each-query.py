class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        N , M = len(items) , len(queries)
        qpairs = [(queries[i] , i) for i in range(M)]
        ans = [0] * M
        items.sort()
        qpairs.sort()
        j = last = 0
        for budget , i in qpairs:
            ans[i] = last
            while j < N and items[j][0] <= budget:
                ans[i] = max(items[j][1] , ans[i])
                j += 1
            last = ans[i]

        return ans
