def angryProfessor(k, a):
    early = 0
    for item in a:
        if item <= 0:
            early += 1
    print(early)
    if early < k:
        return "YES"
    return "NO"