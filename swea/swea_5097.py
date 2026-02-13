def enqueue(item):
    global rear
    rear += 1
    q[rear] = item

def dequeue():
    global front
    front += 1
    return q[front]

t = int(input())
for tc in range(t):
    n, m =map(int, input().split())
    lst = list(map(int, input().split()))
    q = [0] * 1001
    front = -1
    rear = n-1

    for i in range(n):
        q[i] = lst[i]
    
    for _ in range(m):
        save = dequeue()
        enqueue(save)
    
    print(f'#{tc+1} {q[front+1]}')

