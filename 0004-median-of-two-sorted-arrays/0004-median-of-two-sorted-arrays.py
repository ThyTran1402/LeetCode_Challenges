class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length%2==1:
            return self.kthSmallest(nums1, nums2, length // 2)
        else:
            return (self.kthSmallest(nums1, nums2, length // 2) + self.kthSmallest(nums1, nums2, length // 2 - 1)) / 2
        
    def kthSmallest(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        length_a, length_b = len(a) // 2, len(b) // 2
        median_a, median_b = a[length_a], b[length_b]
        
        if length_a + length_b < k: #check if k is bigger than the sum of a and b's median indices
            #if median of an is greater than b, bb's first half does not include k
            if median_a > median_b:
                return self.kthSmallest(a, b[length_b+1:], k - length_b - 1)
            else:
                return self.kthSmallest(a[length_a+1:], b, k - length_a - 1)
        #if k is smaller the sum of a and b's median indices
        else:
            #if median of a is greater than b, a's second half does not include k
            if median_a > median_b:
                return self.kthSmallest(a[:length_a], b, k)
            else:
                return self.kthSmallest(a, b[:length_b], k)
                
#Time complexity: O(log(min(m, n)))-> m, n is length of the first and second array