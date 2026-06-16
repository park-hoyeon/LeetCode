class Solution(object):
    def canVisitAllRooms(self, rooms):
       
        n = len(rooms)
        visited = [False] * (n+1)

        def dfs(x):
            visited[x] = True
            count = 1

            for nx in rooms[x]:
                if not visited[nx]:
                    count += dfs(nx)
            return count
        
        answer = dfs(0)
        return answer == n
