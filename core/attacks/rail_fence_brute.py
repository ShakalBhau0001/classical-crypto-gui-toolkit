def decrypt_rail_fence(ciphertext: str, rails: int) -> str:
    if rails <= 1:
        return ciphertext

    length = len(ciphertext)
    rail = [["\n" for _ in range(length)] for _ in range(rails)]
    row, col = 0, 0
    dir_down = 1

    # Marking zigzag
    for _ in range(length):
        rail[row][col] = "*"
        col += 1
        row += dir_down

        if row == 0 or row == rails - 1:
            dir_down *= -1

    # Filling characters
    index = 0
    for i in range(rails):
        for j in range(length):
            if rail[i][j] == "*" and index < length:
                rail[i][j] = ciphertext[index]
                index += 1

    # Reading zigzag
    result = []
    row, col = 0, 0
    dir_down = 1

    for _ in range(length):
        result.append(rail[row][col])
        col += 1
        row += dir_down

        if row == 0 or row == rails - 1:
            dir_down *= -1

    return "".join(result)


def brute_force(ciphertext: str, max_rails: int = None) -> list:
    if max_rails is None:
        max_rails = max(2, len(ciphertext) // 2)

    results = []

    for rails in range(2, max_rails + 1):
        plaintext = decrypt_rail_fence(ciphertext, rails)

        results.append({"rails": rails, "plaintext": plaintext})

    return results
