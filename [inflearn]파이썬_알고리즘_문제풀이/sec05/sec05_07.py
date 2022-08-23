import sys
# sys.stdin = open("input.txt","r")
'''
교육과정 설계
'''
seq = list(input())
n = int(input())
for i in range(n):
    subject = list(input())
    check = [None]
    for s in subject:
        if s in seq and check[-1] != s:
            check.append(s)
    if seq == check[1:len(seq)+1]:
        print('#{} YES'.format(i+1))
    else:
        print("#{} NO".format(i+1))
