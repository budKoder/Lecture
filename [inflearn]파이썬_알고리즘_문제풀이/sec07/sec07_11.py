import sys
# sys.stdin = open("input.txt", "r")
'''
등산경로
'''
# def DFS(x, y):
#     global cnt
#     if x == ed[0] and y == ed[1]:
#         cnt += 1
#     else:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and a[nx][ny] > a[x][y]:
#                 visited[nx][ny] = 1
#                 DFS(nx, ny)
#                 visited[nx][ny] = 0
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     visited = list([0] * (n+2) for _ in range(n+2))
#     st = [-1, -1]
#     ed = [-1, -1]
#     mi, mx = 2147000000, -2147000000
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] < mi:
#                 mi = a[i][j]
#                 st = [i, j]
#             if a[i][j] > mx:
#                 mx = a[i][j]
#                 ed = [i, j]
#
#     visited[st[0]][st[1]] = 1
#
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     cnt = 0
#     DFS(st[0], st[1])
#     print(cnt)
'''
solution
'''
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)
