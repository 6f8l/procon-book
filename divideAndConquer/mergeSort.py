def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        mergeSort(l)
        mergeSort(r)

        # iはleftのindex
        # jはrightのindex
        # kは元の配列のindex
        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [int(s) for s in list(input().split())]
    mergeSort(arr)
    print(arr)