import math


def _get_column_order(key: str):
    sorted_key = sorted(list(key))
    order = []

    for char in key:
        idx = sorted_key.index(char)
        order.append(idx)
        sorted_key[idx] = None

    return order


def encrypt(text: str, key: str) -> str:
    text = text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    text += "X" * (rows * cols - len(text))
    matrix = []
    index = 0

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)

    order = _get_column_order(key)
    cipher = ""

    for num in sorted(range(cols), key=lambda x: order[x]):
        for r in range(rows):
            cipher += matrix[r][num]

    return cipher


def decrypt(cipher: str, key: str) -> str:
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)
    order = _get_column_order(key)
    matrix = [["" for _ in range(cols)] for _ in range(rows)]
    index = 0
    for num in sorted(range(cols), key=lambda x: order[x]):
        for r in range(rows):
            matrix[r][num] = cipher[index]
            index += 1

    return "".join("".join(row) for row in matrix)
