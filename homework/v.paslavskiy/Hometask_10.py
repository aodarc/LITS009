def tag(name):
    def decorator(foo):
        def wrapper(*args):
            res = ''
            for a in args:
                tag_insert = a
                if name.isdigit() is True:
                    res = 'error'
                elif name.isdigit() is False:
                    res = "<{0}>{1}</{0}>".format(name.lower(), tag_insert.upper())
            return res
        return wrapper
    return decorator


TEST_CASES = [
        ({'name': 'span'}, 'lorem ipsum', '<span>LOREM IPSUM</span>'),
        ({'name': 'div'}, 'lorem ipsum', '<div>LOREM IPSUM</div>'),
        ({'name': 'STRONG'}, 'lorem ipsum', '<strong>LOREM IPSUM</strong>'),
        ({'name': '123'}, 'lorem ipsum', 'error'),
        ({'name': 'h1'}, 'lorem ipsum', '<h1>LOREM IPSUM</h1>'),
        ({'name': [1, 2, 'f', 'g']}, 'lorem ipsum', '<strong>LOREM IPSUM</strong>'),
    ]

for case in TEST_CASES:
    @tag(**case[0])
    def foo(text):
        return text.upper()
    print(foo(case[1]), case[2])
    assert foo(case[1]) == case[2]
