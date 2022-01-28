%%cython

def fib_cy(int n):
    a, b = 1, 1
    for i in range(n):
        a, b = a + b, a

    return a

%time fib_cy(20)