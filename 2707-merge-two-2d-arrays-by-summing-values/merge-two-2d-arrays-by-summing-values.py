class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                # If ids are the same, sum the values
                x = nums1[i][1] + nums2[j][1]
                res = [nums1[i][0], x]
                arr.append(res)
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                # If nums1's id is smaller, add nums1[i]
                arr.append(nums1[i])
                i += 1
            else:
                # If nums2's id is smaller, add nums2[j]
                arr.append(nums2[j])
                j += 1

        # Add remaining elements of nums1 if any
        while i < len(nums1):
            arr.append(nums1[i])
            i += 1

        # Add remaining elements of nums2 if any
        while j < len(nums2):
            arr.append(nums2[j])
            j += 1

        return arr
