import copy
import sys
sys.stdin = open("input.txt", "r")
'''
수열 추측하기
'''
def DFS(L):
    if L >= n:
        num = copy.deepcopy(res)
        while len(num) > 1:
            temp = []
            for j in range(len(num)-1):
                s = num[j] + num[j+1]
                if s > f:
                    return
                else:
                    temp.append(num[j] + num[j+1])
            num = temp
        if num[0] == f:
            for x in res:
                print(x, end=' ')
            sys.exit()
    else:
        for i in range(1, n+1):
            if i not in res:
                res[L] = i
                DFS(L+1)
                res[L] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0] * n
    DFS(0)
