%%Cython 
cpdef float def poly_cy(float a,float b):
    return 10.5 * a + 3 ** b

%time poly_cy(100,10) 


