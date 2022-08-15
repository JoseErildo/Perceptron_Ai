def somatorio(valor1,valor2,bias):
    return valor1+valor2+bias

def funcao_ativacao(somatorio):
    if(somatorio < 0 ):
        return 0
    return 1
    
def label1(w1,w2):
    bias= -1
    x1 = 2
    x2 = 2
    return funcao_ativacao(somatorio(w1*x1,w2*x2,bias))

def label2(w1,w2):
    bias= 2
    x1 = -2
    x2 = -2
    return funcao_ativacao(somatorio(w1*x1,w2*x2,bias))

def saida(label1_value,label2_value):
    bias = -1.5
    x1 = 1
    x2 = 1
    return funcao_ativacao(somatorio(label1_value*x1,label2_value*x2,bias))

entrada1 = [0,1,0,1]
entrada2 = [0,0,1,1]

for i in range(0,len(entrada2),1):
    print("Saida: ", entrada1[i], " ", entrada2[i], " = ", saida(label1(entrada1[i],entrada2[i]),label2(entrada1[i],entrada2[i])))



