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


def factorial_recursion(n):
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)


def fibonacci_recursion(n: int):
    if n <= 2:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def pow_transform(x, y, n=2) -> str:
    return f"{x**n}^{int(y / n)}"


# def factorial_recursion_tqdm_dy(n,bar,m):
#     bar.update(m)
#     if(n==0):
#         return 1
#     return n * factorial_recursion_tqdm_dy(n-1,bar,m)


# def factorial_recursion_tqdm(n):
#     bar = tqdm(total=1000)
#     if(n==0):
#         num = factorial_recursion_tqdm_dy(n,bar,1000)
#     else:
#         num = factorial_recursion_tqdm_dy(n,bar,1000//n)
#         bar.update(1000-1000//n*n+1)
#     bar.close()
#     return num
# def fibonacci_recursion_tqdm_dy(n,bar,m):
#     bar.update(m)
#     if(n<=2):
#         return 1
#     return (fibonacci_recursion_tqdm_dy(n-1,bar,m)
#               +fibonacci_recursion_tqdm_dy(n-2,bar,m))
# def fibonacci_recursion_tqdm(n):
#     bar = tqdm(total=1000)
#     if(n==0):
#         bar.close()
#         return 0
#     else:
#         num = fibonacci_recursion_tqdm_dy(n,bar,1000//n)
#         bar.update(1000-1000//n*n+1)
#     bar.close()
#     return num

if __name__ == "__main__":
    print(list(map(int, bin(int.from_bytes(bytes2gray((0b1010).to_bytes())))[2:])))
    print(
        list(
            map(
                int,
                bin(
                    int.from_bytes(
                        gray2bytes(
                            int("".join(map(str, [1, 1, 1, 1])), base=2).to_bytes()
                        )
                    )
                )[2:],
            )
        )
    )

