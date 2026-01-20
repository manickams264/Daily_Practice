def migratoryBirds(arr):
    max_count = 0
    bird = 0
    for item in set(arr):
        if arr.count(item) >= max_count and item < bird:
            max_count = arr.count(item)
            bird = item 
        elif arr.count(item) > max_count:
            max_count = arr.count(item)
            bird = item
    return bird