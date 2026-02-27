import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum_arr = [0] * n
sum_arr[0] = arr[0]
for i in range(1,n):
    sum_arr[i] = sum_arr[i-1] + arr[i]

print(sum(sum_arr))