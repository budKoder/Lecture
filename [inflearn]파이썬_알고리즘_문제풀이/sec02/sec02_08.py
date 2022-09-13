import sys
# sys.stdin = open("input.txt","r")
'''
뒤집은 소수
'''
def reverse(x):
    result = 0
    while x > 0:
        result = result*10 + x%10
        x //= 10
    return result


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True


n = int(input())
arr = list(map(int, input().split()))
for x in arr:
    rev = reverse(x)
    if isPrime(rev):
        print(rev, end=' ')


'''
solution
'''
def reverse2(x):
    res = 0
    while x > 0:
        t = x%10
        res = res*10 + t
        x //= 10
    return res

def isPrime2(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x%i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse2(x)
    if isPrime2(tmp):
        print(tmp, end= ' ')
