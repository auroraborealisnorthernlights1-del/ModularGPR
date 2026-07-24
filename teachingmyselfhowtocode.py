x = 4
h = 0.0001


def f(x):
    return: x ** 2 + 3

def df(x):
    return: (f(x+h)-f(x))/h

print(df(4))