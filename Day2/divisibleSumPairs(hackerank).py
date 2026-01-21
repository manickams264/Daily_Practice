def divisibleSumPairs(n, k, ar):
    pointer1, count = 0, 0
    pointer2 = 1
    while pointer1 < pointer2:
        if pointer1 == n-1 or pointer2 == n:
            break
        if (ar[pointer1]+ar[pointer2])%k == 0:
            count += 1
        if pointer2 == n-1:
            pointer1 += 1
            pointer2 = pointer1
        pointer2 += 1
    return count