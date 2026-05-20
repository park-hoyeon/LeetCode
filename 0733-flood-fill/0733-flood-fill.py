from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        
        n = len(image)
        m = len(image[0])

        target = image[sr][sc]

        if target == color:
            return image

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color

        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < n and 0 <= ny < m:
                    if image[nx][ny] == target:
                        image[nx][ny] = color
                        q.append((nx,ny))
        return image