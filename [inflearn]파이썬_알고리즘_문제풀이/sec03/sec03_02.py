import sys
# sys.stdin = open("input.txt","r")
'''
숫자만 추출
'''
s = input()
n = 0
for x in s:
    if x.isnumeric():
        n = n*10 + int(x)
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        cnt += 1
print(n, cnt, sep='\n')

'''
solution
'''
# isdigit : 숫자형태는 모두 파악(2^2, 0.1, ...)
# isdecimal : 0 ~ 9
s = input()
res = 0
for x in s:
    if x.isdigit():
        res = res * 10 + int(x)
cnt = 0
for i in range(1, res+1):
    if res%i == 0:
        cnt +=1
print(cnt)
