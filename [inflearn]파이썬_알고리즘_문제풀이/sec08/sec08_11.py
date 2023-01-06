import sys
sys.stdin = open("input.txt", "r")
'''
최대점수 구하기
'''
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# res = [0]*(m+1)
# for score, tm in a:
#     for i in range(m, tm-1, -1):
#         res[i] = max(res[i-tm] + score, res[i])
# print(res[m])
'''
solution
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0]*(m+1)
    for i in range(n):
        ps, pt = map(int, input().split())
        for j in range(m, pt-1, -1):
            dy[j] = max(dy[j], dy[j-pt] + ps)
    print(dy[m])
