#피자굽기 원형큐
def enqueue(item,n):
    global rear
    rear = (rear+1) % n
    q[rear] = item

def dequeue(n):
    global front
    front = (front + 1) % n
    idx, val = q[front]
    return (idx, val//2)

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    lst = list([(i+1, j) for i, j in enumerate(map(int, input().split()))])
    # print(lst)

    q = [0] * n
    for i in range(n):
        q[i] = lst[i]
    
    # print(q)
    front = -1
    rear = n-1

    j = n
    while n != 0:
        save = dequeue(n)

        if j >= m:
            if save[1] == 0:
                rear = (rear+1) % n
                n -= 1
                continue

        elif save[1] == 0:
            save = lst[j]
            j += 1

        enqueue(save,n)

        print(q)

        # if q.count(0) == n-2:
        #     break

    # print(f'#{tc+1} {last_idx}')