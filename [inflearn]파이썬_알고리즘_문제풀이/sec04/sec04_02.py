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

'''
solution
'''
def Count(len):
    cnt = 0
    for x in line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
line = []
res = 0
largest = 0
for _ in range(k):
    tmp = int(input())
    lines.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
