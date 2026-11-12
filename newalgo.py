
def merge(A,B,products):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            products[i+j] = A[i]
            i = i + 1
        else:
            products[i+j] = B[j]
            j = j + 1
    products[i+j:] = A[i:] + B[j:]
    
def mergesort(products):
    if len(products) < 2:
        return None
    mid = len(products) // 2
    A = products[:mid]
    B = products[mid:]
    mergesort(A)
    mergesort(B)
    merge(A,B,products)

def partition(products, i, j):
    pivot = j - 1
    j = pivot - 1
    while i < j:
        while products[i] < products[pivot]:
            i = i + 1
        while i < j and products[j] >= products[pivot]:
            j = j - 1
        if i < j:
            products[i], products[j] = products[j], products[i]
    if products[i] > products[pivot]:
        products[pivot], products[i] = products[i], products[pivot]
        pivot = i
    return pivot

def quicksort(products, left, right):
    if right - left <= 1: return None

    pivot = partition(products, left, right)
    quicksort(products, left, pivot)
    quicksort(products, pivot + 1, right)

def quickselect(products, k):
    left, right = 0, len(products)
    while left < right:
        pivot = partition(products, left, right)
        if k <= pivot:
            right = pivot
        elif k == pivot + 1:
            return products[pivot]
        else:
            left = pivot + 1
    return products[left]



