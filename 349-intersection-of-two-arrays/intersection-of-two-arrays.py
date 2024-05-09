class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newarr = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    newarr.append(j)
        seting = set(newarr)
        listing = list(seting)
        return listing
                
