
def somatorio(valor1,valor2,bias):
    return valor1+valor2+bias

def funcao_ativacao(somatorio):
    if(somatorio < 0 ):
        return 0
    return 1
    
bias=ord("U") *1
w2= ord("U") 
x1 = 1
x2 = -2
w1 = ord(input("Digite uma vogal A, E, I, O, U"))

print(funcao_ativacao(somatorio(w1*x1,w2*x2,bias)))



