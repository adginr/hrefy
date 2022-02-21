import random
import string


def gen_link_short(length: int = 5):
    accetable_chars = string.ascii_letters + string.digits
    return "".join(
        [c for c in random.choice(accetable_chars) for _ in range(1, length)]
    )
