def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    if year < 1918:
        is_leap = (year % 4 == 0)
    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    days_before_sep = 243 if is_leap else 242
    day = 256 - days_before_sep -1
    return f"{day:02d}.09.{year}"