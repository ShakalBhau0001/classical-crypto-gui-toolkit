import re
from collections import Counter


def clean_text(text: str, keep_spaces: bool = False) -> str:
    if keep_spaces:
        return re.sub(r"[^A-Za-z ]", "", text)
    return re.sub(r"[^A-Za-z]", "", text)


def normalize_text(text: str) -> str:
    return text.upper().replace(" ", "")


def chunk_text(text: str, size: int) -> list:
    return [text[i : i + size] for i in range(0, len(text), size)]


def letter_frequency(text: str) -> dict:
    text = clean_text(text).upper()
    return dict(Counter(text))


def index_of_coincidence(text: str) -> float:
    text = clean_text(text).upper()
    n = len(text)

    if n <= 1:
        return 0.0

    freq = Counter(text)
    numerator = sum(f * (f - 1) for f in freq.values())
    denominator = n * (n - 1)

    return numerator / denominator


def is_english_like(text: str, threshold: float = 0.06) -> bool:
    ic = index_of_coincidence(text)
    return ic >= threshold
