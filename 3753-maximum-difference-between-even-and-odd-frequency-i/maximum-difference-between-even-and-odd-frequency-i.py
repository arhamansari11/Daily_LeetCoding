class Solution:
    def maxDifference(self, s: str) -> int:
        set1 = set(s)
        even = []
        odd = []
        for i in set1:
            counting = s.count(i)
            if counting % 2 == 0:
                even.append(counting)
            else:
                odd.append(counting)


        maximum = max(odd)
        minimum = min(even)

        return maximum - minimum