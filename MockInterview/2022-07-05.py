"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

"""
# [  [1,2,1],
#    [1,1,0],
#    [0,1,2]]
# store rotten org into set((0,1), (2,2))
# start from the (0,0)
#    check the 4-direction to check there is rotten org?
#    

# [  [1,2,1],
#    [0,1,1],
#    [1,0,2]]
#
# 1. used visited cell and store 2's location
# 1. use BFS.
# 1. find the val = 2 location and find the longest path.
# 1. traverse each direction 
#     1. the val is 1 then change to 2
#     1. the val is 0 then skip it
def rottenOrange(grid) -> int:
    rotten_org = collections.deque() # (0,1) and (2,2)
    fresh_org = set() # (0,0) (0,2) (1,1) (1,2) (2,0)
    m = len(grid) # 3
    n = len(grid[0]) # 3
    res = 0
    # finding the fresh & rotten org
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotten_org.append((i, j))
            elif grid[i][j] == 1:
                fresh_org.add((i, j))

    if not rotten_org: return -1
    if not fresh_org: return 0

    # start to check the rotting org
    while rotten_org:
        x, y = rotten_org.popleft()

        # check the out of bounds
        if x - 1 > 0 and grid[x-1][y] == 1:
            rotten_org.append((x-1, y))
            fresh_org.remove((x-1, y))
        if y - 1 > 0 and grid[x][y-1] == 1:
            rotten_org.append((x, y-1))
            fresh_org.remove((x, y-1))
        if x + 1 < n and grid[x+1][y] == 1:
            rotten_org.append((x+1, y))
            fresh_org.remove((x+1, y))
        if y + 1 > m and grid[x][y+1] == 1:
            rotten_org.append((x-1, y))
            fresh_org.remove((x-1, y))
            
        res += 1

    if not fresh_org: return -1
    return res



from collections import deque
class Solutions:
    def orangeRotting(self, grid: List[List[int]]) ->:
        """
        BFS
        1. start at the multiple locations
        2. count the number of oranges
        3. locate the rotten oranges put in the queue
        """
        q = deque()
        fresh_oranges = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(len(gird)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    orange += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        # Breath First Search -> level order traversal
        cnt = 0
        visited = set(q)
        while q and fresh_oranges:
            for i in range(len(q)):
                y, x = q.popleft()
                for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)] :
                    my = y + dy
                    nx = x + dx
                    if (-1 < nx < n and -1 < my < m) and grid[my][nx] == 1 and (my, nx) not in visited:
                        q.append((my, nx))
                        visited.add(my, nx)
                        oranges -= 1
                    
        


            cnt +=
        return cut if orange == 0 else -1
        
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS
        1. start at the multiple locations
        2. count the number of oranges
        3. locate the rotten oranges put in the queue
        """
        q = deque()
        oranges = 0
        
        # save all the information
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
                  
        # BFS graph -> level order traversal
        cnt = 0
        visited = set(q)
        while q and oranges:
            n = len(q)
            for _ in range(n):
                y, x = q.popleft()
                for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)]:                    
                    ny = y + dy
                    nx = x + dx
                    if (-1 < ny < len(grid) and -1 < nx < len(grid[0])) and grid[ny][nx] == 1 and (ny, nx) not in visited:
                        q.append((ny, nx))
                        visited.add((ny,nx))
                        oranges -= 1    
                        
            cnt += 1
        
        return cnt if oranges == 0 else -1