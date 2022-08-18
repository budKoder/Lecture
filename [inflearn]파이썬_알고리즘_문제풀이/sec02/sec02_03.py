import sys
# sys.stdin = open("input.txt","r")
'''
K번째 큰 수
'''
n,k = map(int, input().split())
arr = list(map(int, input().split()))
sums = set()
for x in range(n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            sums.add(arr[x]+arr[y]+arr[z])
sums = sorted(sums, reverse=True)
print(sums[k-1])
