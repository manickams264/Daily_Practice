def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for item in arr:
        if item > 0:
            positive_count += 1
        elif item < 0:
            negative_count += 1
        else:
            zero_count += 1
    positive_ratio = positive_count/len(arr)
    negative_ratio = negative_count/len(arr)
    zero_ratio = zero_count/len(arr)
    print(f"{positive_ratio:.6f}")  
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")