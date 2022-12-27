import sys
# sys.stdin = open("input.txt", "r")
'''
단지 번호 붙이기
'''
# def DFS(x, y):
#     for p in range(4):
#         nx = x + dx[p]
#         ny = y + dy[p]
#         if 0<=nx<n and 0<=ny<n and a[nx][ny] == 1:
#             result[idx] += 1
#             a[nx][ny] = 0
#             DFS(nx, ny)
#
#
# def get_sum(a):
#     s = 0
#     for x in a:
#         s += sum(x)
#     return s
#
#
# def find_start_index(a):
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             if a[i][j] != 0:
#                 return i, j
#     return -1, -1
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = [list(map(int, list(input()))) for _ in range(n)]
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     idx = -1
#     result = []
#     while True:
#         if get_sum(a) == 0:
#             break
#         x, y = find_start_index(a)
#         if x == -1 and y == -1:
#             break
#
#         idx += 1
#         result.append(0)
#         DFS(x, y)
#
#     result.sort()
#     print(len(result))
#     for r in result:
#         print(r)
'''
solution
'''
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
            board[xx][yy] = 0
            DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for r in res:
        print(r)
