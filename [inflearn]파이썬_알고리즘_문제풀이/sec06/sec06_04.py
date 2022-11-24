import sys
sys.stdin = open("input.txt", "r")
'''
합이 같은 부분집합(DFS)
'''
def DFS(x, subSum):
    if subSum == total - subSum:
        print("YES")
        sys.exit()
    if x >= n or subSum > total - subSum:
        return
    else:
        DFS(x+1, subSum + a[x])
        DFS(x+1, subSum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")