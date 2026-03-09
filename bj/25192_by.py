import sys
input = sys.stdin.readline

N = int(input())
ans = 0
cnt = 0
d = dict()
i = 0
while i != N:
    i += 1
    word = input().strip()
    # print(word)
    if word == 'ENTER':
        ans += cnt
        cnt = 0
        d = dict()
    else:
        if d.get(word, -1) == -1:
            d[word] = 1
            cnt += 1
ans += cnt
print(ans)