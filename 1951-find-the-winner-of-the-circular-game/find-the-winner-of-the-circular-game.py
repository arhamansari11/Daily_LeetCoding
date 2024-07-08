class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for player_num in range(2, n + 1):
            res: int = (res + k) % player_num
        return res + 1