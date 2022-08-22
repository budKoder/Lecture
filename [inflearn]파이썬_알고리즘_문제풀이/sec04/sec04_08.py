import sys
# sys.stdin = open("input.txt","r")
'''
침몰하는 타이타닉(그리디)
'''
n,m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
left = 0
right = len(w)-1
cnt = 0
while right >= left:
    if w[right] + w[left] <= m:
        left += 1
    cnt += 1
    right -= 1
print(cnt)
