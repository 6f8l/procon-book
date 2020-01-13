def linearSearch(A, key):
    i = 0
    A.append(key)
    n = len(A) - 1
    while A[i] != key:
        i += 1
    if i == n:
        return "NOT_FOUND"
    return i

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split(' ', n)))

    q = int(input())
    T = list(map(int, input().split(' ', q)))

    for tgt in T:
        print(linearSearch(S, tgt))
