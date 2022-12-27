import sys
# sys.stdin = open("input.txt", "r")
'''
사다리 타기
'''
# def DFS(x, y):
#     if x == 0:
#         print(y)
#         sys.exit()
#     else:
#         for i in range(3):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<n and a[nx][ny] == 1:
#                 a[nx][ny] = 0
#                 DFS(nx, ny)
#                 a[nx][ny] = 1
#
#
# if __name__ == "__main__":
#     n = 10
#     a = [list(map(int, input().split())) for _ in range(n)]
#     dx = [0, 0, -1]
#     dy = [-1, 1, 0]
#     x, y = 9, -1
#     for k in range(n):
#         if a[-1][k] == 2:
#             y = k
#             break
#     DFS(x, y)
'''
solution
'''
def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        # 왼쪽
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        # 오른쪽
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        # 위
        else:
            DFS(x-1, y)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):     # 열
        if board[9][y] == 2:
            DFS(9, y)
