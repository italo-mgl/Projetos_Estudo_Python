def f(x):
    resultado = 1 + x
    return resultado


print(f(2))

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """Juros_compostos serve para calcular a taxa de juros de acordo com o aporte financeiro,
      taxa e ano de investimento.
      
        aporte:
            um numero inteiro, que represente o valor em R$.

        taxa:
            um número float entre 0 e 1 que represente o valor taxa de juros.

        anos:
            um numero inteiro  >= 1 que representa o tempo que o investimento terá liquidez.
    
    """
    return aporte * (1 + taxa) ** anos

print(juros_compostos(aporte=1000, taxa=0.13, anos=4))


juros_compostos