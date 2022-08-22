import sys
# sys.stdin = open("input.txt","r")
'''
랜선자르기(결정알고리즘)
'''
k,n = map(int, input().split())
lines = []
for _ in range(k):
    l = int(input())
    lines.append(l)

low = 1
high = max(lines)
while high >= low:
    mid = (high+low)//2
    cnt = 0
    for l in lines:
        cnt += l//mid

    if cnt >= n:
        low = mid+1
    elif cnt < n:
        high = mid-1

print(high)
