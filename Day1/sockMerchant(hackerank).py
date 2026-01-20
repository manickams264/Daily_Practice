def sockMerchant(n, ar):
    unique = []
    count = 0
    for item in ar:
        if item not in unique:
            unique.append(item)
        elif item in unique:
            unique.remove(item)
            count += 1
    return count