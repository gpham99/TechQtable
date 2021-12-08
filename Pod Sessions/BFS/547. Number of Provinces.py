from queue import Queue
class Solution:
    def BFS(self, isConnected, i, q, visited):
        visited.add(i)
        q.put(i)
        
        while not q.empty():
            i = q.get()
            for j in range(len(isConnected[i])):      
                if j not in visited and isConnected[i][j] == 1:
                    visited.add(j)
                    q.put(j)
    
    def findCircleNum(self, isConnected) -> int:
        n_province = 0
        visited = set()
        q = Queue()
        for i in range(len(isConnected)): # isConnected[i] ~ vertex
            if i not in visited:
                n_province += 1
                self.BFS(isConnected, i, q, visited)
        return n_province