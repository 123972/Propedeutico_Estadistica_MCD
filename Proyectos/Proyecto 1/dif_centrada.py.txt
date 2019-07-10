def aprox_derivada_centrada(x,fun,h=0.0000001):
    dfun = (fun(x+h)-fun(x-h))/(2*h)
    return dfun

def aprox_segunda_derivada_centrada(x,fun,h=0.0000001):
    ddfun = (fun(x+h)-2*fun(x)+fun(x-h))/(h**2)
    return ddfun

