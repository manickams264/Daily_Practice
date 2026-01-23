def countingValleys(steps, path):
    altitude = 0
    valley = 0
    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valley += 1
        else:
            altitude -= 1
    return valley