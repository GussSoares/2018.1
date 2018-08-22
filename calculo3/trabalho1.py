#
# Posição Falsa
#

def posicaoFalsa(a,b,e1,e2,max,ajuste):
    if (b-a) <= e1:                 # se b-a for menor que epslon, a raiz está no intervalo
        raiz = [a,b]
        return raiz
    if abs(ajuste*a – a*ln(a)) < e2:
        raiz = a
        return raiz
    if abs(ajuste*b – b*ln(b)) < e2:
        raiz = b
        return raiz
    k = 0

