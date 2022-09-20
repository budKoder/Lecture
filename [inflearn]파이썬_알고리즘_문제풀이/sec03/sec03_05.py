import sys
# sys.stdin = open("input.txt","r")
'''
수들의 합
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

if sum(a) < m:
    cnt = 0
elif sum(a) == m:
    cnt = 1
else:
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += a[j]
            if sum == m:
                cnt += 1
            if sum > m:
                break
print(cnt)

'''
solution
'''
# tot : lt~rt바로 앞까지의 합
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
