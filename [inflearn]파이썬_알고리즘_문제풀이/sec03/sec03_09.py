import sys
# sys.stdin = open("input.txt","r")
'''
봉우리
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# padding
for i in range(n):
    arr[i].insert(0,0)
    arr[i].append(0)
arr.insert(0,[0]*(n+2))
arr.append([0]*(n+2))
# 봉우리
cnt = 0
for row in range(1,len(arr)-1):
    for col in range(1,len(arr)-1):
        cur = arr[row][col]
        # up, down, left, right
        surround = [arr[row-1][col], arr[row+1][col], arr[row][col-1], arr[row][col+1]]
        if cur > max(surround):
            cnt += 1
print(cnt)

'''
solution
'''
# left, up, right, down
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
