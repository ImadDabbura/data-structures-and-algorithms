def bucket_sort(L, k):
    n = len(L)
    bucket = [[] for _ in range(k + 1)]
    for e in L:
        bucket[e].append(e)
    output = [0] * n
    i = 0
    for k in bucket:
        for e in k:
            output[i] = e
            i += 1
    return output
