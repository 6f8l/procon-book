def bubbleSort(N, A):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
    return A


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split(' ', N)))
    print(bubbleSort(N, A))
