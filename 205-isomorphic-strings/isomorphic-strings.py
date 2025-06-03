class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for s1 , t1 in zip(s , t):
            if s1 in s_to_t:
                if s_to_t[s1] != t1:
                    return False

            elif t1 in t_to_s:
                if t_to_s[t1] != s1:
                    return False

            else:
                s_to_t [s1] = t1
                t_to_s [t1] = s1

        return True