import cProfile
import random
k = 10

def part(arr, left, right):
    pivot = arr[right]
    idx = left
    for i in range(left, right):
        if arr[i] > pivot:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    arr[idx], arr[right] = arr[right], arr[idx]
    return idx

def kthElement(arr, left, right, k):
    idx = part(arr, left, right)
    if idx == k:
        return arr[idx]
    if idx > k:
        return kthElement(arr, left, idx - 1, k)
    else:
        return kthElement(arr, idx + 1, right, k)

for a in range(100,8000,400):
    arr = []
    for i in range(0, a):
        s = random.randrange(0, 101)
        arr.append(s)

    print(a)
    cProfile.run('[kthElement(arr, 0, a - 1, k) for i in range(10000)]')