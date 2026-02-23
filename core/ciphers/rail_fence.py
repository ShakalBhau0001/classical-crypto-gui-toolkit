def encrypt(text: str, rails: int) -> str:
    if rails < 2:
        raise ValueError("Rails must be >= 2")

    text = text.replace(" ", "")
    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for char in text:
        fence[row].append(char)
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    return "".join("".join(r) for r in fence)


def decrypt(cipher: str, rails: int) -> str:
    if rails < 2:
        raise ValueError("Rails must be >= 2")

    pattern = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for _ in cipher:
        pattern[row].append("*")
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(len(pattern[r])):
            pattern[r][c] = cipher[index]
            index += 1

    result = []
    row = 0
    direction = 1

    for _ in cipher:
        result.append(pattern[row].pop(0))
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    return "".join(result)
