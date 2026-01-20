def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_count, min_count = 0, 0
    for item in range(1,len(scores)):
        if scores[item] < min_score:
            min_score = scores[item]
            min_count += 1
        if scores[item] > max_score:
            max_score = scores[item]
            max_count += 1
    return [max_count, min_count]
