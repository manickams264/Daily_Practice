def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [item+a for item in apples]
    oranges = [item+b for item in oranges]
    apple_count, orange_count = 0, 0
    for item in apples:
        if item>=s and item<=t:
            apple_count+=1
    for item in oranges:
        if item>=s and item<=t:
            orange_count+=1
    print(apple_count,orange_count,sep='\n')