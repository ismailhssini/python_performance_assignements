%load_ext Cython
%%Cython 
def poly_cy(a,b):
    return 10.5 * a + 3 ** b

%prun poly_cy(100,10) 


