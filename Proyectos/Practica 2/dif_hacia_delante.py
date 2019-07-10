def aprox_derivada_delante(x,fun,h=0.0000001):
    dfun = (fun(x+h)-fun(x))/h
    return dfun

def aprox_segunda_derivada_delante(x,fun,h=0.0000001):
    ddfun = (fun(x+2*h)-2*fun(x+h)+fun(x))/h**2
    return ddfun
