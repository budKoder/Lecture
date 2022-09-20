import sys
# sys.stdin = open("input.txt","r")
'''
곶감
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 회전
m = int(input())
for _ in range(m):
    row, direction, distance = map(int, input().split())
    row -= 1
    distance %= n
    if distance > 0:
        new = []
        if direction == 0:
            new = arr[row][distance:]+arr[row][:distance]
        else:
            new = arr[row][-distance:]+arr[row][:-distance]
        arr[row] = new

# 합
mid = n//2
cnt = arr[mid][mid]
st,ed = mid, mid+1
for i in range(mid):
    st -= 1
    ed += 1
    cnt += sum(arr[mid-(i+1)][st:ed])
    cnt += sum(arr[mid+(i+1)][st:ed])
print(cnt)

'''
solution
'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            arr[h-1].append(arr[h-1].pop(0))
    else:
        for _ in range(k):
            arr[h-1].insert(0, arr[h-1].pop())
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
