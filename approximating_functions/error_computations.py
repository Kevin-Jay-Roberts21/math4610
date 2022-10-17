def absolute_error(u, v):
    error = abs(u - v)
    print("Absolute Error: " + str(error))
    return error

def relative_error(u, v):
    error = abs(u - v)/abs(u)
    print("Relative Error: " + str(error))
    return error