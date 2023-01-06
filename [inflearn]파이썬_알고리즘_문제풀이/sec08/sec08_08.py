import sys
sys.stdin = open("input.txt", "r")
'''
알리바바와 40인의 도둑(Top-Down)
'''
# def DFS(x, y):
#     if d[x][y] != 0:
#         return d[x][y]
#     if x == 0 and y == 0:
#         return a[0][0]
#     else:
#         mi = 2147000000
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 val = DFS(nx, ny)
#                 if mi > val:
#                     mi = val
#         d[x][y] = mi + a[x][y]
#         return d[x][y]
#
#
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# d = [[0]*n for _ in range(n)]
# dx = [-1, 0]
# dy = [0, -1]
# print(DFS(n-1, n-1))
'''
solution
'''
def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    print(DFS(n-1, n-1))
