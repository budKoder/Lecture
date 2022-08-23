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
