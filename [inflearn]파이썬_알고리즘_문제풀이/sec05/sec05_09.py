import sys
# sys.stdin = open("input.txt", "r")
'''
Anagram(아나그램)
'''
a = input()
b = input()
check_a, check_b = dict(), dict()
for x in a:
    if x in check_a:
        check_a[x] += 1
    else:
        check_a[x] = 1
for y in b:
    if y in check_b:
        check_b[y] += 1
    else:
        check_b[y] = 1
if check_a == check_b:
    print("YES")
else:
    print("NO")
