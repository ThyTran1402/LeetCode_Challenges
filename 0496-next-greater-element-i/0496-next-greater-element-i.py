class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        #result = []
        
        for i in nums2:
            while stack and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
            
            result = [-1] * len(nums1)
            
        for index, i in enumerate(nums1):
            if i in hashmap:
                result[index] = hashmap[i]
        return result