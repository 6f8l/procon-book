def selectionSort(N, A):
    # iは配列の順番を示している
    for i in range(0, N-1):
        # iより小さい数値はすでにソート済みの数値
        min_j = i
        # jはまだソート済みじゃない数値
        for j in range(i, N):
            # i番目の数値よりもj番目の数値が大きい場合、i番目とj番目の数値を入れ替える
            print(A[j])
            if A[j] < A[min_j]:
                min_j = j
        A[i], A[min_j] = A[min_j], A[i]
    return A

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split(' ', N)))
    print(selectionSort(N, A))