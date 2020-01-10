# This function uses tmp var
def shellsort_shift(arr):
    gap = len(arr) // 2

    while gap > 0:
        for right in range(gap, len(arr)):
            key = arr[right]
            left = right
            while left >= gap and key < arr[left - gap]:
                arr[left] = arr[left - gap]
                left -= key
            arr[left] = key
        gap //= 2
    return arr

# This function does not use tmp var
def shellsort_swap(arr):
    gap = len(arr) // 2

    while gap > 0:
        for right in range(gap, len(arr)):
            left = right
            while left >= gap and arr[left] < arr[left - gap]:
                arr[left - gap], arr[left] = arr[left], arr[left - gap]
                left -= gap
        gap //= 2
    return arr

if __name__ == "__main__":
    from random import shuffle
    l = range(15)
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(shellsort_shift(l))
    assert l == lcopy
