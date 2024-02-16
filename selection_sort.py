def selection_sort(A: list):
    for j in range(0, len(A)):
        min_index = j
        for i in range(j + 1, len(A)):
            if A[i] < A[min_index]:
                min_index = i
        A[j], A[min_index] = A[min_index], A[j]
    return A

print(selection_sort([64,25,12,22,11]))