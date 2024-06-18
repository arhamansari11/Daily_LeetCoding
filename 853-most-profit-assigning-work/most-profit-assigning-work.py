class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = sorted(zip(difficulty , profit))
        worker.sort()

        best_profit = 0
        max_profit = 0
        i = 0

        for ability in worker:
            while i < len(job) and job[i][0] <= ability:
                best_profit = max(best_profit , job[i][1])
                i += 1
            max_profit += best_profit
        
        return max_profit