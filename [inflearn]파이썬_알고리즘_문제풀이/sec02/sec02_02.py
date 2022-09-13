import sys
# sys.stdin = open("input.txt","r")
'''
K번째 수
'''
t = int(input())
for i in range(t):
    n,s,e,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr[s-1:e] = sorted(arr[s-1:e])
    print("#{} {}".format(i+1, arr[s+k-2]))

'''
solution
'''
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print(a[k-1])
