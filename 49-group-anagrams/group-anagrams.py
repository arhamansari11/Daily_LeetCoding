class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)

        return list(dic.values())