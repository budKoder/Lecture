import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
'''
토마토
'''
# if __name__ == "__main__":
#     m, n = map(int, input().split())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     dq = deque()
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 1:
#                 dq.append([i, j])
#     res = 0
#     while dq:
#         size = len(dq)
#         ck = False
#         for _ in range(size):
#             x, y = dq.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0<=nx<n and 0<=ny<m and a[nx][ny] == 0:
#                     dq.append([nx, ny])
#                     a[nx][ny] = 1
#                     ck = True
#         if ck:
#             res += 1
#
#     for row in a:
#         if any(x == 0 for x in row):
#             print(-1)
#             break
#     else:
#         print(res)
'''
solution
'''
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
dis = [[0]*n for _ in range(m)]     # 익는데 걸리는 날짜
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0<=xx<m and 0<=yy<n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            Q.append((xx, yy))
flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
