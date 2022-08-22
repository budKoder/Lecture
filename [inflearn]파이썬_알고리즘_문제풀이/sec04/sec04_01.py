import sys
# sys.stdin = open("input.txt","r")
'''
이분검색
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = n
while right >= left:
    mid = (left+right)//2
    if arr[mid] == m:
        break
    elif arr[mid] < m:
        left = mid+1
    else:
        right = mid-1
print(mid+1)
