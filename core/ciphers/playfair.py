import string


def build_matrix(keyword: str, merge_letter: str = "I"):
    keyword = keyword.upper().replace(" ", "")

    if merge_letter not in ["I", "J"]:
        raise ValueError("merge_letter must be 'I' or 'J'")

    remove_letter = "J" if merge_letter == "I" else "I"

    seen = set()
    key_string = ""

    for ch in keyword:
        if ch == remove_letter:
            ch = merge_letter
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            key_string += ch

    for ch in string.ascii_uppercase:
        if ch == remove_letter:
            continue
        if ch not in seen:
            seen.add(ch)
            key_string += ch

    return [list(key_string[i : i + 5]) for i in range(0, 25, 5)]


def _find_position(matrix, letter):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == letter:
                return r, c


def _process_text(text: str, merge_letter: str):
    text = text.upper().replace(" ", "")
    replace_letter = "J" if merge_letter == "I" else "I"
    text = text.replace(replace_letter, merge_letter)
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    if len(pairs[-1]) == 1:
        pairs[-1] += "X"

    return pairs


def encrypt(text: str, keyword: str, merge_letter: str = "I") -> str:
    matrix = build_matrix(keyword, merge_letter)
    pairs = _process_text(text, merge_letter)
    cipher = ""

    for a, b in pairs:
        r1, c1 = _find_position(matrix, a)
        r2, c2 = _find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt(text: str, keyword: str, merge_letter: str = "I") -> str:
    if not keyword.strip():
        raise ValueError("Keyword cannot be empty.")

    matrix = build_matrix(keyword, merge_letter)

    text = text.upper().replace(" ", "")
    pairs = [text[i : i + 2] for i in range(0, len(text), 2)]

    plain = ""

    for a, b in pairs:
        r1, c1 = _find_position(matrix, a)
        r2, c2 = _find_position(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]
        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain
