import sys
sys.stdin = open("input.txt", "r")
'''
네트워크 선 자르기(Bottom-Up)
'''
# n = int(input())
# f = [0] * (n+1)
# f[1] = 1
# f[2] = 2
# for i in range(3, n+1):
#     f[i] = f[i-1] + f[i-2]
# print(f[n])

'''
solution
f(n) = f(n-1) + f(n-2)
'''
n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]
print(dy[n])
