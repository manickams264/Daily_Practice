def birthday(s, d, m):
    count = 0
    for index in range(len(s)-m+1):
        if sum(s[index:index+m]) == d:
            count += 1
    return count