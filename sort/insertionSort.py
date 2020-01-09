import random

def insertionSort(arr, N):
    for i in range(1, N):  # iは選択中の数値の並び順
        v = arr[i]
        j = i - 1 # jは選択中の数値の一つ前の番号の並び順

        while j >= 0 and arr[j] > v: # 並び順が0以上 == 不適でない && 選択中の数値の一つ前の値が選択中の値より大きい場合
            arr[j+1] = arr[j] # j番目の数値を一つ後ろにずらす
            j -= 1 # jを一つずつ小さくしていく
        arr[j+1] = v # 選択中の値をずらして空になった箇所に挿入する
    return arr

if __name__ == "__main__":
    arr = []
    for i in range(0, 10):
        arr.append(random.randint(0, 100))
    arranged_arr = insertionSort(arr, len(arr))
    print(arranged_arr)