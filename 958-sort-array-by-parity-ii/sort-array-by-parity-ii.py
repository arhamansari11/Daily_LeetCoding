class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        parity = [] 
        for i in range(len(even)):
            parity.append(even[i]) 
            parity.append(odd[i]) 
        
        return parity