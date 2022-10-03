import sys
# sys.stdin = open("input.txt","r")
'''
단어 찾기
'''
n = int(input())
note = list()
used = list()
for _ in range(n):
    note.append(input())
for _ in range(n-1):
    used.append(input())
print(list(set(note)-set(used))[0])

'''
solution
'''
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items():
    if val == 1:
        print(key)
        break
