def hoare(A, l, r):
    # A[l] , A[(l+r)//2], A[r]을 비교해서 중간값 찾기
    if A[l] <=  A[(l+r)//2] <= A[r]:
        A[l], A[(l+r)//2] = A[(l+r)//2], A[l]
    elif A[l] <= A[r] <=  A[(l+r)//2]:
        A[l], A[r] = A[r], A[l]

    pivot = A[l]
    i, j = l, r # i 피봇보다 큰 값을 찾아 이동, j 작은값을 찾아 이동
    while i<=j:
        while i<=j and A[i] <= pivot:   # 피봇보다 큰 값을 만날때까지 이동
            i += 1
        while i<=j and A[j] >= pivot:   # 피봇보다 작은 값을 만날때까지 이동
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j            # 확정된 위치 리턴

def qsort(arr, l, r):   # l 정렬할 구간의 왼쪽 인덱스, r 오른쪽 인덱스
    if l < r:   # 구간에 두 개 이상의 원소가 있는 경우
        p = hoare(arr, l, r) # pivot의 위치 정하기
        qsort(arr, l, p-1)
        qsort(arr, p+1, r)

a = list(map(int, input().split()))
N = 1000000

qsort(a, 0, N-1)
print(a[500000])