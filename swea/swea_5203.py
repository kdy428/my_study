t = int(input())

for tc in range(1, t+1):
    cards = list(map(int, input().split()))

    p1 = []
    p2 = []
    winner = 0

    for i in range(6): # idx : 0 1 2 3 4 5
        p1.append(cards[2 * i])
        p2.append(cards[2 * i + 1])

        if 2 <= i:
            p1.sort()
            p2.sort()

            j = 0
            while j <= i-2: 
                if p1[j] == p1[j+1] and p1[j+1] == p1[j+2]:
                    winner = 1
                    break
                if  p1[j] + 1 == p1[j+1] and p1[j+1] + 1 == p1[j+2]:
                    winner = 1
                    break
                
                if p2[j] == p2[j+1] and p2[j+1] == p2[j+2]:
                    winner = 2
                    break
                if  p2[j] + 1 == p2[j+1] and p2[j+1] + 1 == p2[j+2]:
                    winner = 2
                    break
                j += 1
        
            if winner != 0:
                break

    print(f'#{tc} {winner}')
