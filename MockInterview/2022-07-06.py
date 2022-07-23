"""
1584. Min Cost to Connect All Points
Medium

2600

74

Add to List

Share
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


MST - Minimun Spanning Tree

1. Kruscal - Union Find
2. Prime's - Priority Queue == heap


1. graph {a:[b,c,d,]...}
    {a:(1,b), (2,c), (3, d)}
verticies
2.  BFS

Greedy, priority queue == heap
a -> 

"""
# 1. pick one v and calc e val and find the min one and keep add into res value

def MinCostToConnectAllPoints(points):
    # res = 0
    
    # for i in range(len(points)):
    #     x1, y1 = point[i] # -2, 5
    #     curMin = float("inf")
        
    #     for j in range(i+1, len(points)):
    #         x2, y2 = point[j] # -4, 1
    #         curMin = min(curMin, abs(x2-x1) + abs(y2-y1)) # min (inf, 6) = 6
            
    #     res += curMin # 12 + 6

    # return res # 18
    # minimun spanning tree? 
    g = 
    
    

from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        graph = defaultdict(list)
        
        for i in range(N):
            x1 = points[i][0]
            y1 = points[i][1]
            
            for j in range(i+1, N):
                
                x2 = points[j][0]
                y2 = points[j][1]
                cost = abs(x1-x2) + abs(y1-y2)
                
                graph[i].append((cost, j))
                graph[j].append((cost, i))
"""

defaultdict(<class 'list'>, 
{0: [(4, 1), (13, 2), (7, 3), (7, 4)],
1: [(9, 2), (5, 3), (7, 4)], 
2: [ (14, 4)], 
3: [(7, 0), (3, 1), (10, 2), (4, 4)], 
4: [(7, 0), (7, 1), (14, 2), (4, 3)]})

visited = 0,1,3
"""

        res = 0
        h = [(0,0)]
        visited = set()
           
        while h and len(visited) < N:
            
            cost, node = heappop(h) # 14, 4
            
            if node in visited:
                continue
            res += cost # 4 + 5
            visited.add(node) # 3
            
            for new_weight, new_node in graph[node]: # g[3]
                
                heappush(h, (new_weight, new_node))
                
        return res