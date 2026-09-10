# region perfect_square_blah_blah_blah
def perfect_square_plus_gs(a, b) -> str:
    """完全平方和公式

    给定 `(a + b) ** 2` 中的 `a` `b`，
    将给定的值填入后输出 `a**2 + b**2 + 2*a*b` 这一字符串。

    返回的结果应当是合法的python表达式
    """
    return f"{a}**2 + {b}**2 + 2*{a}*{b}"


def perfect_square_plus_z(a, b):
    return a**2 + b**2 + 2*a*b  # fmt: skip


def perfect_square_sub_gs(a, b) -> str:
    """完全平方差公式

    给定 `(a - b) ** 2` 中的 `a` `b`，
    将给定的值填入后输出 `a**2 + b**2 - 2*a*b` 这一字符串。

    返回的结果应当是合法的python表达式
    """
    return f"{a}**2 + {b}**2 - 2*{a}*{b}"


def perfect_square_sub_z(a, b):
    return a**2 + b**2 - 2*a*b  # fmt: skip


# endregion


def bytes2gray(data: bytes) -> bytes:
    """
    将 bytes 中的每个字节按位转换为格雷码（Gray code）。
    规则：gray = binary ^ (binary >> 1)
    """
    return bytes(bytearray(b ^ (b >> 1) for b in data))


def gray2bytes(data: bytes) -> bytes:
    """
    将格雷码转换回原始二进制数据（逐字节逆向）。
    格雷码转二进制的规则：从高位到低位，逐位异或。
    """
    result = bytearray()
    for g in data:
        binary = g
        mask = binary >> 1
        while mask:
            binary ^= mask
            mask >>= 1
        result.append(binary)
    return bytes(result)


def base_conversion(x, y):
    l = []  # noqa: E741
    t = x
    while t > 0:
        l.append(t % y)
        t //= y
    l.reverse()
    return l


def base_conversion_dex(x):
    t3 = "".join(map(str, x))
    return int(t3, 2)


def fibonacci_recursion(n: int):
    if n <= 2:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def pow_transform(x, y, n=2) -> str:
    return f"{x**n}**{y // n}"
