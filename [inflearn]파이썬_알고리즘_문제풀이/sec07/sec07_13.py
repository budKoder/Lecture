import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
'''
섬나라 아일랜드
'''
# def BFS(sx, sy):
#     dq = deque()
#     dq.append([sx, sy])
#     a[sx][sy] = 0
#     while dq:
#         x, y = dq.popleft()
#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0<=nx<n and 0<=ny<n and a[nx][ny] == 1:
#                 a[nx][ny] = 0
#                 dq.append([nx, ny])
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#
#     dx = [-1, 0, 1, 0, -1, -1, 1, 1]
#     dy = [0, -1, 0, 1, -1, 1, -1, 1]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == 1:
#                 BFS(i, j)
#                 cnt += 1
#     print(cnt)
'''
solution
'''
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt += 1
print(cnt)
