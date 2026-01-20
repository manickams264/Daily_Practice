def bonAppetit(bill, k, b):
    total = 0
    for item in range(len(bill)):
        if item != k:
            total += bill[item]
    total = total//2
    if total == b:
        print("Bon Appetit")
    else:
        difference = abs(total - b)
        print(difference)