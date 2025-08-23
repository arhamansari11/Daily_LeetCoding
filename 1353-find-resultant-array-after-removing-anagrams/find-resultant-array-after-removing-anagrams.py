class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]   
        for i in range(1, len(words)):
            sort_curr = "".join(sorted(words[i]))
            sort_prev = "".join(sorted(ans[-1]))
            if sort_curr != sort_prev: 
                ans.append(words[i])
        return ans
