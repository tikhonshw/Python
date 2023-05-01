def generator(lis):
    for i in lis:
        yield i

val = generator([6, 9, 2, 5])
print(next(val))
print("Something")
print(next(val))
print(next(val))
print(next(val))
