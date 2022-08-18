import sys
# sys.stdin = open("input.txt","r")
'''
회문 문자열 검사
'''
def check(s):
    mid = len(s)//2
    for i in range(mid):
        if s[i] != s[-1-i]:
            return False
    return True


n = int(input())
for i in range(n):
    s = input().upper()
    print("#{} {}".format(i+1, "YES" if check(s) else "NO"))
