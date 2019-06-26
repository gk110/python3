def myfunc(*args):
    out = []
    for i in args:
        if i%2 == 0:
           out.append(i)
    return out

print (myfunc (2,4,6,8,1))