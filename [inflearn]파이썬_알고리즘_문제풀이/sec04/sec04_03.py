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

'''
solution
'''
def Count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n,m = map(int, input().split())
music = list(map(int, input().split()))
maxx = max(music)   # 가장 큰 곡을 담을 수 있어야 한다.
lt = 1
rt = sum(music)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
