def largestIsland(grid):
    n=len(grid)
    visited = [[0]*n for _ in range(n)]
    component_size = [[0]*n for _ in range(n)]
    component_id = [[0]*n for _ in range(n)]
    maxi = 0
    k = 1

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i,j)]
                g = [(i,j)]
                visited[i][j] = 1
                while stack:
                    r, c = stack.pop()
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = 1
                            stack.append((nr, nc))
                            g.append((nr, nc))
                l = len(g)
                for x, y in g:
                    component_size[x][y] = l
                    component_id[x][y] = k
                k += 1
                maxi = max(maxi, l)
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                # print(i,j)
                ans=1
                dir=(((-1,0),(0,1),(1,0),(0,-1)))
                o=[]
                for x,y in dir:
                    if 0<=i+x<n and 0<=j+y<n:
                        # print(component_id[i+x][j+y],i+x,j+y)
                        if visited[i+x][y+j]==1 and (len(o)==0 or component_id[i+x][j+y] not in o):
                            ans+=component_size[i+x][j+y]
                            o.append(component_id[i+x][j+y])
                maxi=max(maxi,ans)
    
    return maxi

print(largestIsland([[1,0],[1,1]]))
        
                
                        
