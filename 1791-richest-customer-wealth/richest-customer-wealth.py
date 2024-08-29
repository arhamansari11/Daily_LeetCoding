class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0

        for i in range(len(accounts)):
            addition = sum(accounts[i])
            if wealth < addition:
                wealth = addition

        return wealth