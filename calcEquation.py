# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:09:38 2023

@author: priya
"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        for i, (var1, var2) in enumerate(equations):
            graph[var1].append((var2, values[i]))
            graph[var2].append((var1, 1.0 / values[i]))
            
        res = []
        
        def dfs(node, res):
            if node == end:
                return res
            visited.add(node)
            for neigh, val in graph[node]:
                if neigh not in visited:
                    score = dfs(neigh, res * val)
                    if score != -1:
                        return score
            return -1
                    
        for start, end in queries:
            visited = set([])
            if start not in graph or end not in graph:
                res.append(-1)
            else:
                res.append(dfs(start, 1))
        
        return res