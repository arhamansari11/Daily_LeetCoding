class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        boolean = False
        if len(arr) >= 3:
            for i in range(len(arr)-2):
                if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                    boolean = True
                    break

        return boolean