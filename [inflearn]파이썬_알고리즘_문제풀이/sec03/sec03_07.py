import sys
# sys.stdin = open("input.txt","r")
'''
사과나무
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
st, ed = 0, n
mid = n//2
cnt = sum(arr[mid])
for i in range(mid):
    st += 1
    ed -= 1
    cnt += sum(arr[mid-(i+1)][st:ed])
    cnt += sum(arr[mid+(i+1)][st:ed])
print(cnt)

'''
solution
'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
