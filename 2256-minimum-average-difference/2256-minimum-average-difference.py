class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        leftSums = [nums[0]]
        totalSum = nums[0]
        for i in range(1, len(nums)):
            leftSums.append(leftSums[-1]+nums[i])
            totalSum += nums[i]
            
        idx = 0
        answer = 10000000000
        leftCount = 0
        for i in range(len(nums)):
            leftCount += 1
            rightCount = len(nums) - leftCount
            left_sum = leftSums[i]
            right_sum = totalSum - left_sum
            leftAvg = left_sum // leftCount
            if rightCount == 0:
                rightAvg = 0
            else:
                rightAvg = right_sum // rightCount
            diff = abs(leftAvg - rightAvg)
            if diff < answer:
                answer = diff
                idx = i
        return idx