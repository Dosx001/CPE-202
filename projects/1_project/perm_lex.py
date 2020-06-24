def perm_gen_lex(x):
    x = list(x)
    a = []
    if len(x) == 2:
        return [x[0]+x[1], x[1]+x[0]]
    for i in range(len(x)):
        y = x.pop(i)
        z = perm_gen_lex(x)
        a += [y + ii for ii in z]
        x.insert(i, y)
    if len(x) == 1:
        return x
    return a
