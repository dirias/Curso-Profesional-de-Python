def password_validator(func):
    def wrapper(pw):
        func(pw)
        if len(pw) > 8:
            print('The password is strong enough')
        else:
            print('The password is too week, please change it')

    return wrapper

@password_validator
def login(pw):
    pass

login('hola')