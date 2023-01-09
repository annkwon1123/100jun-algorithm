n_of_call = 0
result = -1
def merge_sort(A, p, r):  # A[p..r]을 오름차순 정렬한다.
    if p < r:
        q = int((p+r) / 2)       # q는 p, r의 중간 지점
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i] 
            t += 1
            i += 1 # tmp[t] <- A[i]; t++; i++;
        else:
            tmp[t] = A[j]
            t += 1
            j += 1 # tmp[t] <- A[j]; t++; j++;
 
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        t += 1
        j += 1
    i = p
    t = 1
    
    global n_of_call
    global k
    global result
    while i <= r:  # 결과를 A[p..r]에 저장
        n_of_call += 1
        A[i] = tmp[t]
        if n_of_call == k:
            result = A[i]
        i += 1
        t += 1

n, k = map(int, input().split())
A = list(map(int, input().split()))
print(result)
