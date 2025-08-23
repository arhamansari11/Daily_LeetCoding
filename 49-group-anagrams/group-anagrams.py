class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            sort = sorted(i)
            sorting = "".join(sort)
            if sorting not in dic:
                dic[sorting] = [i]
            else:
                dic[sorting] += [i]
        ans = []
        for i , j in dic.items():
            ans.append(j)


        return ans