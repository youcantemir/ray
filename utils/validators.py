def has_upper(password):

    return any(c.isupper() for c in password)

def has_lower(password):

    return any(c.islower() for c in password)

def has_digit(password):

    return any(c.isdigit() for c in password)

def has_symbol(password):

    return any(not c.isalnum() for c in password)
