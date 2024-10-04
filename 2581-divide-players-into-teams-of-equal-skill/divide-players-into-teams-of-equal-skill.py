class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        result = []
        while l <= r:
            result.append((skill[l] , skill[r]))
            l += 1
            r -= 1
        tupples = []
        for i in result:
            tupples.append(sum(i))
        unique = set(tupples)
        ans = []
        if len(unique) == 1:
            for i in result:
                ans.append(i[0] * i[1])
        else:
            return -1
        return sum(ans)

        

