import sys
# sys.stdin = open("input.txt",'r')
'''
자릿수의 합
'''
def digit_sum(x):
    result = 0
    while x > 0:
        result += x%10
        x //= 10
    return result


n = int(input())
arr = list(map(int, input().split()))
result = []
for idx, val in enumerate(arr):
    result.append([idx, val, digit_sum(val)])
result.sort(key=lambda x:(x[2],-x[0]), reverse=True)
print(result[0][1])

'''
solution
'''
n = int(input())
a = list(map(int, input().split()))

def digit_sum1(x):
    sum = 0
    while x > 0:
        sum += x%10
        x //= 10
    return sum

def digit_sum2(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
