import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dic_a = dict()
for i in a:
    dic_a[i] = 1

m = int(input())
b = list(map(int, input().split()))
for j in b:
    if dic_a.get(j):
        print(1)
    else:
        print(0) 