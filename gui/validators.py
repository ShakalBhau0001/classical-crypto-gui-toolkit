def validate_int(value: str):
    if not value.isdigit():
        raise ValueError("Key must be numeric.")
    return int(value)


def validate_string(value: str):
    value = value.strip()
    if not value:
        raise ValueError("Key cannot be empty.")
    if len(set(value)) != len(value):
        raise ValueError("Duplicate characters not allowed in key.")
    return value
