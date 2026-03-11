import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(int(input()) for _ in range(n)))
i = 0
j = n-1
tmp = 2000000000
# 음수가 존재
while i < j:
    gap = arr[j] - arr[i]
    if gap >= m:
        # m보다 크면서 이전 값보다 차이가 작으면
        if gap - m <= tmp:
            tmp = gap - m
            output = gap
        else:
            j -= 1
            i = 0
    else:
        break
    i += 1
    
print(output)
