# This method is implemented in open address method

def h1(key):
    return key % m

def h2(key):
    return 1 + (key % (m-1))

def h(key, i):
    return (h1(key) + i * h2(key)) % m

def insert(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[j] == None:
            return j
        else:
            i = i + 1

def search(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[j] == key:
            return j
        elif T[j] == None or i >= m:
            return None
        else:
            i = i + 1
    return

def hashingMethod():
    return

if __name__ == "__main__":
    hashingMethod()