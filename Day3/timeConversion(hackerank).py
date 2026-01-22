def timeConversion(s):
    s = s.split(':')
    time = ''
    if 'PM' in s[-1]:
        if s[0] == '12':
            s[0] = '12'
        else:
            s[0] = int(s[0])
            s[0] += 12
            s[0] = str(s[0])
        time += s[0] + ':'
        time += s[1] + ':'
        for item in s[-1]:
            if item not in ['P','M']:
                time += item
    else:
        if s[0] == '12':
            s[0] = '00'
        time += s[0] + ':'
        time += s[1] + ':'
        for item in s[-1]:
            if item not in ['A','M']:
                time += item
    return time