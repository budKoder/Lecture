import sys
sys.stdin = open("input.txt", "r")
'''
바둑이 승차(DFS)
'''
def DFS(x, subSum, leftSum):
    global mx
    if subSum > c:
        return
    elif subSum + leftSum < mx:
        return
    elif x >= n:
        if subSum > mx:
            mx = subSum
    else:
        DFS(x+1, subSum + w[x], leftSum - w[x])
        DFS(x+1, subSum, leftSum - w[x])


if __name__ == "__main__":
    c, n = map(int, input().split())
    w = list(int(input()) for _ in range(n))
    mx = 0
    DFS(0, 0, sum(w))
    print(mx)
