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


if __name__ == "__main__":
    n = int(input())
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 2
    print(DFS(n))
