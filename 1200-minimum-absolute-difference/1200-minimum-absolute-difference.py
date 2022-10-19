class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDif = math.inf
        arr.sort() # sort in ascending order
        dict = collections.defaultdict(list)
        
        for i in range(len(arr)-1):
            curDif = arr[i+1] - arr[i]
            dict[curDif].append([arr[i], arr[i+1]])
            minDif = min(minDif, curDif)
        return dict[minDif]
            

#sort the array first; traverse through the array; find the differece between two numbers     
#Time complexity: O(NlogN)
#Space complexity: O(N)