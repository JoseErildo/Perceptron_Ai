Segunda  = [1, 0, 1, 0, 1, 1, 0]
Terca = [0, 1, 1, 0, 1, 0,0]
Quarta = [1, 1, 1, 1, 0, 1, 1]
Quinta = [0, 1, 1, 1, 1, 0, 1]
Sexta = [1,  0, 1, 0, 0, 0, 1]
Sabado = [1, 0, 1, 1, 1, 1, 0]
Domingo = [1, 1, 1, 1, 1, 1, 1]

SemanaAnterior = [0,0,1,1,1,0,1]


#Semana passada (já que o mais recente) + Taxa de frequencia do dia/2

#+ clima

def somatorio(valor1,valor2,bias):
    return valor1+valor2+bias

def funcao_ativacao(somatorio):
    if(somatorio < 0 ):
        return 0
    return 1
    
def returnTemperatura(valor):
    if(valor == 1):
        return 0.5
    return 0.4

def DiaSemana(valor):
    global Segunda 
    global Terca 
    global Quarta 
    global Quinta 
    global Sexta 
    global Sabado 
    global Domingo
    global SemanaAnterior 

    if(valor == 1):
        return (sum(Domingo)/len(Domingo) + sum(SemanaAnterior)/7)/2
    elif(valor == 2):
        return (sum(Segunda)/len(Segunda) + sum(SemanaAnterior)/7)/2
    elif(valor == 3):
        return (sum(Terca)/len(Terca) + sum(SemanaAnterior)/7)/2
    elif(valor == 4):
        return (sum(Quarta)/len(Quarta) + sum(SemanaAnterior)/7)/2
    elif(valor == 5):
        return (sum(Quinta)/len(Quinta) + sum(SemanaAnterior)/7)/2
    elif(valor == 6):
        return (sum(Sexta)/len(Sexta) + sum(SemanaAnterior)/7)/2
    else:
        return (sum(Sabado)/len(Sabado) + sum(SemanaAnterior)/7)/2

def appendDiaSemana(dia,resultadoDoDia):
    global Segunda 
    global Terca 
    global Quarta 
    global Quinta 
    global Sexta 
    global Sabado 
    global Domingo
    global SemanaAnterior 

    if(dia == 1):
        Domingo.append(dia)
    elif(dia == 2):
        Segunda.append(dia)
    elif(dia == 3):
        Terca.append(dia)
    elif(dia == 4):
        Quarta.append(dia)
    elif(dia == 5):
        Quinta.append(dia)
    elif(dia == 6):
        Sexta.append(dia)
    else:
        Sabado.append(dia)
    
dia = int(input("Dia da Semana (1-Domingo, 2-Segunda, 3-Terça ... 7-Sábado"))
bias = -1
w2 = returnTemperatura(int(input("Clima:  1 - Quente,   2 - Nublado")))
x1 = 1
x2 = 1
w1 = DiaSemana(dia)

print(funcao_ativacao(somatorio(w1*x1,w2*x2,bias)))
appendDiaSemana(dia,funcao_ativacao(somatorio(w1*x1,w2*x2,bias)))