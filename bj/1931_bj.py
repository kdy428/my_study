import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort(key=lambda x: (x[1], x[0]))
cnt = 0
i = 0
tmp = 0
while i < n:
    if lst[i][0] >= tmp:
        cnt += 1
        tmp = lst[i][1]
    i += 1

print(cnt)