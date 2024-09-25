class Solution:
    def reverseString(self, nums: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        def Reverse(arr , l , r):
            if l >= r:
                return
            else:
                arr[l] , arr[r] = arr[r] , arr[l]
                return Reverse(arr , l+1 , r-1)
        l = 0
        r = len(nums) - 1
        return Reverse(nums , l , r )