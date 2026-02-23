def brute_force(ciphertext: str) -> list:
    results = []

    for shift in range(1, 26):
        left_result = ""
        right_result = ""

        for char in ciphertext:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")

                # Left shifting (decrypting)
                left_result += chr((ord(char) - base - shift) % 26 + base)

                # Right shifting (encrypting)
                right_result += chr((ord(char) - base + shift) % 26 + base)
            else:
                left_result += char
                right_result += char

        results.append({"shift": shift, "direction": "left", "plaintext": left_result})

        results.append(
            {"shift": shift, "direction": "right", "plaintext": right_result}
        )

    return results
