def comparison_counting_sort(A):
    n = len(A)
    Count = [0] * n
    S = [0] * n

    for i in range(n):
        Count[i] = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] < A[j]:
                Count[j] += 1
                print(f"A[{i}] < A[{j}]: Count[{j}] = {Count[j]}")
            else:
                Count[i] += 1
                print(f"A[{i}] >= A[{j}]: Count[{i}] = {Count[i]}")

    for i in range(n):
        S[Count[i]] = A[i]

    print("\nIntermediate arrays:")
    print("Count:", Count)
    print("S:", S)

    return S

# Input list
A = [60, 35, 81, 98, 14, 47]

print("Input List:", A)
sorted_array = comparison_counting_sort(A)
print("\nSorted Array:", sorted_array)
