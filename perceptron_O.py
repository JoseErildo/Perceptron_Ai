
def somatorio(valor1,valor2,bias):
    return valor1+valor2+bias

def funcao_ativacao(somatorio):
    if(somatorio < 0 ):
        return 0
    elif (somatorio == 0):
        return 1
    return 0

bias = -79
w2 = 158
x1 = -1
x2 = 1
w1 = ord(input("Digite uma vogal A, E, I, O, U"))

print(funcao_ativacao(somatorio(w1*x1,w2*x2,bias)))



