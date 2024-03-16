import random, string


def generate_session_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
