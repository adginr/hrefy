import string
import typing as ty

ALPHABET = string.ascii_letters + string.digits

ALPHABET_MAP = dict((c, idx) for (idx, c) in enumerate(ALPHABET))
BASE = len(ALPHABET_MAP)


def num_encode(num: int) -> str:
    """Encode num and return string"""
    encoded: list[str] = []
    while True:
        num, r = divmod(num, BASE)
        encoded.append(ALPHABET[r])
        if num == 0:
            break

    return "".join(encoded)
