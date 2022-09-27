import sys
# sys.stdin = open("input.txt",'r')
'''
마구간 정하기(결정알고리즘)
'''
n,c = map(int, input().split())
location = []
for _ in range(n):
    location.append(int(input()))
location.sort()
low = 1
high = max(location)
while high >= low:
    mid = (low+high)//2
    point = location[0]
    cnt = 1
    for i in range(1,len(location)):
        if location[i] >= point + mid:
            cnt += 1
            point = location[i]

    if cnt >= c:
        low = mid+1
    else:
        high = mid-1
print(high)

'''
solution
'''
def Count(len):
    cnt = 1
    ep = line[0]
    for i in range(1, n):
        if line[i] - ep >= len:
            cnt += 1
            ep = line[i]
    return cnt


n,c = map(int, input().split())
line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()
lt = 1
rt = line[n-1]
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
