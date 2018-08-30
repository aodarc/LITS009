def tag(name='<div>', name2=''):
    def decorator(func):
        def wrapper(*args2):
            try:
                if name2 == '':
                    new_name = str(name).replace('<', '</')
                    return name + func(*args2) + new_name
                else:
                    return name + func(*args2) + name2
            except TypeError:
                err = 'You input incorrect *args, plz write one or two args of type str in @'
                err += tag.__name__
                print(err)
        return wrapper
    return decorator


@tag(name='<div>')
def foo():
    return 'lorem ipsum'

print(foo())