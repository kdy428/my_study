# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = 0

# def func(idx, sum_v):
#     global ans
#     if idx == n:
#         return
#     if sum_v + arr[idx] == m:
#         ans += 1
    
#     func(idx+1, sum_v+arr[idx])
#     func(idx+1, sum_v)

# func(0, 0)
# print(ans)

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    for comb in combinations(arr, i):
        if sum(comb) == m:
            ans += 1
print(ans)