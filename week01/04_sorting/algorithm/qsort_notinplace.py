def partition(arr, p):
    l, r = [], []
    for i in range(1, len(arr)):
        if arr[i] < p:
            l.append(arr[i])
        else:
            r.append(arr[i])
    return l, r


def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        l, r = partition(arr, pivot)
        ls = quick_sort(l)
        rs = quick_sort(r)
        return ls + [pivot] + rs
    else:
        return arr
