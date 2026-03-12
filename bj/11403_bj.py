import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
d = defaultdict(list)
for i in range(1, n+1):
    count = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if count[j]:
            d[i].append(j)
            d[j].append(i)
print(d)