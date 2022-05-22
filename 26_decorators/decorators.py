import functools

user = {"username": "pepe", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)  # keeps the name and docs of get_admin_password function
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return '1234'
    elif panel == "billing":
        return 'password'


print(get_password("billing"))
print(get_password.__name__)
