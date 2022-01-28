def ft_concatenate(l_strings, d):
    """concatenate list of strings into one string separated by delimeter"""
    res = l_strings[0]
    for e in l_strings[1:]:
        res = res + d + e
    return res

def ft_concatenate1(l_strings, d):
    """concatenate list of strings into one string separated by delimeter"""
    res = d.join(l_strings)
    return res

x=10**70000
x=str(x)
d="_"
%prun ft_concatenate(x,d)
%prun ft_concantenate1(x,d)


    
