class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = sum(accounts[0])

        for i in range(1 , len(accounts)):
            addition = sum(accounts[i])
            if wealth < addition:
                wealth = addition

        return wealth