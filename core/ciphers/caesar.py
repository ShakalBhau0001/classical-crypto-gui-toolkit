def encrypt(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)
