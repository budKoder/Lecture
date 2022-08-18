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