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

'''
solution
'''
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 100
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    if money > res:
        res = money
print(res)
