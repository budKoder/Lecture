import sys
# sys.stdin = open("input.txt","r")
'''
K번째 약수
'''
def get_divisor(n):
    result = []
    for i in range(1,n+1):
        if n%i == 0:
            result.append(i)
    return result


n, k = map(int, input().split())
divisor = get_divisor(n)
if len(divisor) < k:
    print(-1)
else:
    print(divisor[k-1])
