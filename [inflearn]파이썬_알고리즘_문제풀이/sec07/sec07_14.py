import sys
from collections import deque
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)    # 재귀리미트 설정
'''
안전영역
'''
# def BFS(sx, sy):
#     q = deque()
#     q.append([sx, sy])
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<n and tmp[nx][ny] != 0:
#                 tmp[nx][ny] = 0
#                 q.append([nx, ny])
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     mi, mx = 2147000000, -2147000000
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] < mi:
#                 mi = a[i][j]
#             if a[i][j] > mx:
#                 mx = a[i][j]
#
#     res = -2147000000
#     for h in range(mi+1, mx):
#         tmp = []
#         for row in a:
#             tmp.append(list(map(lambda x: x if x>h else 0, row)))
#         cnt = 0
#         for i in range(n):
#             for j in range(n):
#                 if tmp[i][j] != 0:
#                     BFS(i, j)
#                     cnt += 1
#         if cnt > res:
#             res = cnt
#     print(res)
'''
solution
'''
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and board[xx][yy] > h:
            ch[xx][yy] = 1
            DFS(xx, yy, h)
            ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)
