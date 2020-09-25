n = int(input())
array = list(map(int, input().split()))
cnt = 0


def mergeSort(p, r):

    if (p < r):
        q = (p + r )// 2
        mergeSort(p, q)
        mergeSort(q + 1, r)
        merge(p, q, r)


def merge(p, q, r):
    global cnt
    n1 = q - p + 1
    n2 = r - q
    i = 0
    j = 0
    L = array[p:q + 1]
    R = array[q + 1:r + 1]
    while (i < n1 and j < n2):
        if L[i] <= R[j]:
            array[p + i + j] = L[i]
            i += 1
        else:
            array[p + i + j] = R[j]
            j += 1
            cnt += q - i - p + 1
    while (i < n1):
        array[p + i + j] = L[i]
        i += 1
    while (j < n2):
        array[p + i + j] = R[j]
        j += 1

mergeSort(0,n-1)
print(cnt)

