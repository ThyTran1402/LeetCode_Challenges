class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDq, minDq = deque(), deque()
        result = 0
        right, left = 0, 0
        for right in range(len(nums)):
            while maxDq and nums[maxDq[-1]] <= nums[right]:
                maxDq.pop()
            while minDq and nums[minDq[-1]] >= nums[right]:
                minDq.pop()
            maxDq.append(right)
            minDq.append(right)
            
            while nums[maxDq[0]] - nums[minDq[0]] > limit:
                left += 1
                if maxDq[0] < left:
                    maxDq.popleft()
                if minDq[0] < left:
                    minDq.popleft()
            result = max(result, right-left+1)
        return result
        
#sling window use 2 deques
# maxDq to keep track of max element in the window range; if we meet a new element that is larger then we 
# pop all smaller elements out of maxDq; the front of maxDq is the max of the current window range
# minDq to keep track of min element in the winfow range; if we meet a new element that is smaller then we
# pop all larger elements out of minDq; the front of minDq is the min of current window range
#Time/Space complexity: O(N)