def count_sort(L, R):
    """Count sort using 0-k(inclusive) integers as the keys."""
    n = len(L)
    count = [0] * (R + 1)

    # count number of elements equal to index i
    for e in L:
        count[e + 1] += 1

    # cumsum of count where count[i] will be the number of elements <= index i
    for i in range(R):
        count[i + 1] += count[i]

    # Distribute the data into the correct order
    tmp = [0] * n
    for e in L:
        tmp[count[e]] = e
        count[e] += 1

    # copy the output back
    for i, e in enumerate(tmp):
        L[i] = e
