class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        number = len(graph)-1
        answer = []
        
        def backtrack(currentNode, path):
            #check if we reach the target, no need to check further
            if currentNode == number:
                answer.append(list(path))
                return
            for next_neighbor in graph[currentNode]: #traverse through the neighbor nodes in the graph
                path.append(next_neighbor)
                backtrack(next_neighbor, path)
                path.pop()
                
        path = [0]
        backtrack(0, path)
        return answer
    
#backtrack approach
#Time complexity: O(2^N.N)
#Space complexity: O(N)