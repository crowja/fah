def myfunc(x=1):
    while True:
        yield x
        x += 2

mynums0 = myfunc(0)
mynums1 = myfunc(1)
print(next(mynums1))
print(next(mynums0))
print(next(mynums1))
print(next(mynums0))
print(next(mynums1))
print(next(mynums0))
