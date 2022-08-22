import sys
# sys.stdin = open("input.txt","r")
'''
뮤직비디오(결정알고리즘)
'''
n,m = map(int, input().split())
music = list(map(int, input().split()))
low = max(music)
high = 10000
while high >= low:
    mid = (low+high)//2
    cnt = 1
    current = 0
    for x in music:
        current += x
        if current > mid:
            current = x
            cnt += 1

    if cnt <= m:
        high = mid-1
    else:
        low = mid+1
print(low)
