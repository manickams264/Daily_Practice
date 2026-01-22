def twoStrings(s1, s2):
    common = 0
    for item in s1:
        if item in s2:
            common = 1
    if common:
        return "YES"
    return "NO" 