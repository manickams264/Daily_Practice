def findDigits(n):
    number, count = n, 0
    while n > 0:
        remainder = n % 10
        if remainder == 0:
            continue
        elif number%remainder == 0:
            count += 1
        n = n // 10 
    return count