class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        addition = sum(rolls)
        remaining_sum = mean * (n + len(rolls)) - addition
        if remaining_sum > (6*n) or remaining_sum < n:
            return []
        else:
            n_arr =[1] * n
            remaining_sum -= n
            for i in range(n):
                add_sum = min(5 , remaining_sum)
                n_arr[i] += add_sum
                remaining_sum -= add_sum

            return n_arr