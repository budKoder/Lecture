import sys
# sys.stdin = open("input.txt","r")
'''
주사위 게임
'''
def getPrice(arr):
    s = set(arr)
    if len(s) == len(arr):
        return max(arr)+100
    elif len(s) == len(arr)-1:
        return 1000+arr[1]*100
    else:
        return 10000+arr[0]*1000


n = int(input())
prices = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    prices.append(getPrice(arr))
print(max(prices))