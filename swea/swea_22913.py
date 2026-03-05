n, k = map(int, input().split())
out = k
lst = [i for i in range(1,n+1)]
ans = []
for i in range(n):
    for j in range(k-1):
        temp = lst.pop(0)
        lst.append(temp)
    ans.append(lst.pop(0))
print(*ans)