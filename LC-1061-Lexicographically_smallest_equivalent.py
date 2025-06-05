# i/p - str1: "parker"
#     - str2: "morris"
# baseStr -   "parser"
# o/p - str: "makkek"
from collections import defaultdict

class Solution:
    def DFS(self, adj, visited, curr):
        visited[ord(curr)-ord('a')]=1
        minChar= curr

        for neighbor in adj[curr]:
            if visited[ord(neighbor)-ord('a')]==0:
                minChar= min(minChar, self.DFS(adj, visited, neighbor))
        return minChar

    def lexically_equivalent(self, str1:str, str2:str, baseStr:str) -> str:
        n = len(str1)
        adj = defaultdict(list)
        res = ""

        for i in range(n):
            u = str1[i]
            v = str2[i]

            adj[u].append(v)
            adj[v].append(u)

        for ch in baseStr:
            visited=[0]*26
            res+=self.DFS(adj, visited, ch)

        return res
