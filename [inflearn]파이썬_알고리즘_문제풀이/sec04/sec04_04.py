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
