import random, string


def generate_session_id() -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
