class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        temp = s.split()
        max_num = -1
        for x in temp:
            if x.isdigit():
                if int(x) > max_num:
                    max_num = int(x)
                else:
                    return False
        return True