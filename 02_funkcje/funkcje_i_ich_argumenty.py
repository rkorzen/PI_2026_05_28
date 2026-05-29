def add(a, b, *args, to_float=False):

    result = a + b + sum(args)
    if to_float:
        return float(result)
    return result

add(a=1, b=2)
print(add(b=1, a=2))

print(add(a=1, b=2, to_float=True))
add(1, 2,3, 4, 5, 6, to_float=True)


add(1, 2, 3, to_float=True)


def add(a, b, *,  to_float=False):

    result = a + b
    if to_float:
        return float(result)
    return result

# print(add(1, 2, 0))
print(add(1, 2, to_float=True))

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo()

foo(1, 2, 3)

foo(c=1, d=2)

foo(1, 2, 3, c=1, d=2)


