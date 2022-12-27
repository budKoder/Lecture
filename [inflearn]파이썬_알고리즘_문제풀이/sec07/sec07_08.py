import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
'''
사과나무
'''
# if __name__ == "__main__":
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     ch = [[0]*n for _ in range(n)]
#     q = deque()
#     q.append([n//2, n//2])
#     result = a[n//2][n//2]
#     ch[n//2][n//2] = 1
#
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     for i in range(n//2):
#         for j in range(len(q)):
#             item = q.popleft()
#             for d in range(4):
#                 nx = item[0] + dx[d]
#                 ny = item[1] + dy[d]
#                 if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0:
#                     result += a[nx][ny]
#                     ch[nx][ny] = 1
#                     q.append([nx, ny])
#     print(result)
'''
solution
'''
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n = int(input())
a = list(map(int, input().split()) for _ in range(n))
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2] = 1
sum += a[n//2][n//2]
Q.append((n//2, n//2))
L = 0
while True:
    if L == n//2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1
print(sum)
