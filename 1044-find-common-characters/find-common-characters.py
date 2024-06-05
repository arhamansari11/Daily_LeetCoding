class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words:
            curr_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c] , curr_cnt[c])

        res = []
        for i in cnt:
            for c in range(cnt[i]):
                res.append(i)

        return res