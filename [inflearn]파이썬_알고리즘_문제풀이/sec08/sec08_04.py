import sys
sys.stdin = open("input.txt", "r")
'''
최대 부분 증가수열
'''
# n = int(input())
# a = list(map(int, input().split()))
# f = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if a[j] < a[i]:
#             f[i] = max(f[i], f[j] + 1)
# print(max(f))
'''
solution
'''
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n+1)
dy[1] = 1
res = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]
print(res)
