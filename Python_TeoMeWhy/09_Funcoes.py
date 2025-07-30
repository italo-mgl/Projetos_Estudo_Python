def f(x):
    resultado = 1 + x
    return resultado


print(f(2))

def juros_compostos(aporte, taxa, anos):
    return aporte * (1 + taxa) ** anos

print(juros_compostos(aporte=1000, taxa=0.13, anos=4))