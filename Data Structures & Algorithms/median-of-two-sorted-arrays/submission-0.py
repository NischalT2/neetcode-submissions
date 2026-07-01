class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        nums1.sort()
        l = len(nums1)
        mid = l // 2
        
        if l % 2 == 0:
            return (nums1[mid] + nums1[mid - 1]) / 2
        else:
            return nums1[mid]

    