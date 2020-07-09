def count_sort(L, k):
    """Count sort using 0-k(inclusive) integers as the keys."""
    n = len(L)
    count = [0] * (k + 1)

    # count number of elements equal to index i
    for e in L:
        count[e] += 1

    # cumsum of count where count[i] will be the number of elements <= index i
    for i in range(1, k + 1):
        count[i] += count[i - 1]

    # copy the output
    output = [0] * n
    for e in L:
        output[count[e] - 1] = e
        count[e] -= 1
    return output
