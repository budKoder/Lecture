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