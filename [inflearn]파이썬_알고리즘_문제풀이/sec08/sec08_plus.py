import sys
sys.stdin = open("input.txt", "r")
'''
계단오르기
'''
def DFS(x):
    if f[x] > 0:
        return f[x]
    else:
        f[x] = DFS(x-1) + DFS(x-2)
        return f[x]


n = int(input())
f = [0] * (n+1)
f[1] = 1
f[2] = 2
print(DFS(n))

'''
돌다리 건너기
'''
n = int(input())
f = [0] * (n+2)
f[1] = 1
f[2] = 2
for i in range(3, n+2):
    f[i] = f[i-1] + f[i-2]
print(f[n+1])
