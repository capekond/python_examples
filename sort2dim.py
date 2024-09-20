li = [[1, 0.23], [2, 0.39], [4, 0.31], [5, 0.27]]
a = sorted(li, key=lambda l: l[1])
print(a)

def foo(a, b, c):
    x = 4
    y = {a:1}
    print (all(list(locals().values())))

foo(1,2,3)