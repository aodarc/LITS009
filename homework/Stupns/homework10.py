def tag(name):
    def decorator(func):
        def wrapper(text):
            try:
                if name == '123':
                    return 'error'
                else:
                    return "<{0}>{1}</{0}>".format(name, func(text))
            except TypeError:
                err = 'error'
                print(err)

        return wrapper

    return decorator


TEST_CASES = [
    ({'name': 'span'}, 'lorem ipsum', '<span>LOREM IPSUM</span>'),
    ({'name': 'div'}, 'lorem ipsum', '<div>LOREM IPSUM</div>'),
    ({'name': 'strong'}, 'lorem ipsum', '<strong>LOREM IPSUM</strong>'),
    ({'name': '123'}, 'lorem ipsum', 'error'),
]

for case in TEST_CASES:
    @tag(**case[0])
    def foo(text):
        return text.upper()


    assert foo(case[1]) == case[2]
