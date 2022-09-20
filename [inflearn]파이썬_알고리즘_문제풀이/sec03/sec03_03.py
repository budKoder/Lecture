import sys
# sys.stdin = open("input.txt","r")
'''
카드 역배치
'''
cards = list(range(1,21))
for _ in range(10):
    ai, bi = map(int, input().split())
    cards[ai-1:bi] = reversed(cards[ai-1:bi])
print(*cards)

'''
solution
'''
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')
