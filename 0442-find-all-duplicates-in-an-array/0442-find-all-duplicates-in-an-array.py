class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = [] #store all duplicate numbers
        for i in nums:
            #if the number at {abs(i)-1}'th index is negative
            if nums[abs(i)-1] < 0:
                answer.append(abs(i)) #we meet a duplicate
            else: #if the number at {abs(i)-1}'th index is positive 
                nums[abs(i)-1] *= -1 #mark it as negative
        return answer
    
#hash map to store the frequency of all numbers with more than 1
#Time complexity: O(N)
#Space complexity: O(1)