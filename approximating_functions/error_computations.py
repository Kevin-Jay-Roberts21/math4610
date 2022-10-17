def absolute_error(u, v):
    error = abs(u - v)
    print(error)
    return error

def relative_error(u, v):
    error = abs(u - v)/abs(u)
    print(error)
    return error

def absolute_digit_accuracy():
    pass