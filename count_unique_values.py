import random

def count_unique(L):
    T = []
    for x in L:
        if x not in T:
            T.append(x)
    return len(T)

def count_unique1(L):
    return len(set(L))

L = [random.random() for i in range(50000)]

%time count_unique(L)
%time count_unique1(L)