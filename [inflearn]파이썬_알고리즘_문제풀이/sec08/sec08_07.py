import sys
sys.stdin = open("input.txt", "r")
'''
알리바바와 40인의 도둑(Bottom-Up)
'''
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# d = [[2147000000]*n for _ in range(n)]
# d[0][0] = a[0][0]
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# for i in range(n):
#     for j in range(n):
#         for k in range(4):
#             nx = i + dx[k]
#             ny = j + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 d[nx][ny] = min(d[nx][ny], d[i][j] + a[nx][ny])
# print(d[n-1][n-1])

'''
solution
'''
if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    dy[0][0] = arr[0][0]
    for i in range(n):
        # 가장자리
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
    print(dy[n-1][n-1])
