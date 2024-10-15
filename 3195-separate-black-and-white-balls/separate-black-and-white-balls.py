class Solution:
    def minimumSteps(self, s: str) -> int:
        l_steps = 0
        ans = 0 
        for i in s:
            if i == '1':
                l_steps += 1
            elif i == '0':
                ans += l_steps


        return ans
