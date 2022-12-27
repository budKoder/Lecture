import sys
sys.stdin = open("input.txt", "r")
'''
알파코드
'''
# def DFS(L):
#     global cnt
#     if L == len(code):
#         print(''.join(result))
#         cnt += 1
#         return
#     else:
#         for i in range(1, 3):
#             if L+i <= len(code):
#                 s = int(''.join(code[L:L+i]))
#                 if 1 <= s <= 26:
#                     result.append(chr(s+64))
#                     DFS(L+i)
#                     result.pop()
#                 else:
#                     return
#
#
# if __name__ == "__main__":
#     code = list(input().strip())
#     cnt = 0
#     result = []
#     DFS(0)
#     print(cnt)
'''
solution
'''
def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
                res[P] = i
                DFS(L+2, P+1)


if __name__ == '__main__':
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)  # 마지막 자리에서 n+1자리까지 확인해야 하므로 dummy 삽입
    res = [0] * (n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
