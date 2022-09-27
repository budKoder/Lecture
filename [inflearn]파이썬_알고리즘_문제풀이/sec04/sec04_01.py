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

'''
solution
'''
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1