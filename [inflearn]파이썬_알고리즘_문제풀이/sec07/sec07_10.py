import sys
# sys.stdin = open("input.txt", "r")
'''
미로탐색
'''
# def DFS(x, y):
#     global cnt
#     if x == n-1 and y == n-1:
#         cnt += 1
#     else:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<n and a[nx][ny] == 0 and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 DFS(nx, ny)
#                 visited[nx][ny] = 0
#
#
# if __name__ == "__main__":
#     n = 7
#     a = [list(map(int, input().split())) for _ in range(n)]
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     cnt = 0
#     visited = list([0] * n for _ in range(n))
#     visited[0][0] = 1
#     DFS(0, 0)
#     print(cnt)
'''
solution
'''
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)
