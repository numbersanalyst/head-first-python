from flask import session
from functools import wraps


def check_logged_in(func: object) -> object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'NIE jesteś zalogowany'
    return wrapper
