class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.split()[::-1])[::-1]
        
        return ' '.join(x[::-1] for x in s.split())
    

# step 1: split the string
# step 2" reverse the string
# step 3: converse each element to string separated by space
# step 4: reverse the string

#Time complexity: O(N)
# Space compplexity: O(1)