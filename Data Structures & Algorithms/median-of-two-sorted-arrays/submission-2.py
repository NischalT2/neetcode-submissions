class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2  # bc index and mid1 & mid2 start at 0

            Aleft = A[mid1] if mid1 >= 0 else float("-infinity")
            Aright = A[mid1 + 1] if (mid1 + 1) <= (len(A) - 1) else float("infinity")
            Bleft = B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2 + 1] if (mid2 + 1) <= (len(B) - 1) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = mid1 - 1
            else:
                l = mid1 + 1
            