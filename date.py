from calendar import _monthlen  # pyright: ignore[reportAttributeAccessIssue]


def month_length(y: int, m: int) -> int:
    return _monthlen(y, m)
