def binarySearch(list, item):
    left = 0
    right = len(list) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == item:
            result = mid
            return result
        elif list[mid] > item:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split(' ', n)))

    q = int(input())
    T = list(map(int, input().split(' ', q)))

    ans = 0

    for i in T:
        if binarySearch(S, i) == None:
            pass
        else:
            ans += 1
    print(ans)