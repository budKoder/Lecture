import sys
from collections import deque
sys.stdin = open("input.txt", "r")
'''
미로의 최단거리 통로
'''
# if __name__ == "__main__":
#     n = 7
#     a = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[0] * n for _ in range(n)]
#     q = deque()
#     q.append([0, 0])
#     visited[0][0] = 1
#
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#
#     while q:
#         x, y = q.popleft()
#         if x == n-1 and y == n-1:
#             break
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0<=nx<n and 0<=ny<n and a[nx][ny] == 0 and visited[nx][ny] == 0:
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append([nx, ny])
#     print(visited[n-1][n-1] - 1)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
