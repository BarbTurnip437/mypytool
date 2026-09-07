from calendar import isleap


def month_first_day(day, week):
    day %= 7
    if day == 0:
        day = 7
    return week - (day - 1)


def month_length(y: int, m: int) -> int:
    if m == 2:
        if isleap(y):
            return 29
        else:
            return 28
    elif m in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    else:
        return 30
