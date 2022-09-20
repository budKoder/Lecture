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

'''
solution1
'''
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("%d NO"%(i+1))
            break
    else:
        print("#%d YES"%(i+1))

'''
solution2
'''
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES"%(i+1))
    else:
        print("%d NO"%(i+1))
