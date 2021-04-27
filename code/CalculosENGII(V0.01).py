#ENG II 26/04/21
def area_circuferencia(raio):
    """calcula a area de uma circuferencia"""
    area = 3.14 * (raio * raio)
    return area

def perimetro_circuferencia(raio):
    """Calcula o perimetro de uma circuferencia"""

    perimetro = 2 * 3.14 * raio
    return perimetro

def area_retangulo():
    """calcula a area do retangulo"""
    return area

def perimetro_retangulo():
    """calcula o perimetro do retangulo"""
    return perimetro

opcao = -1
while opcao != 0:
    print('Escolha a opção desejada')
    print()
    print('1 -cálculo da área da circuferencia ')
    print('2 -cálculo do perimetro da circuferencia')
    print('3 -cálculo da área do retangulo')
    print('4 -cálculo do perimetro do retangulo')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
       
       raio = float(input('Entre com o valor do raio, para obter a área: '))
       area = 3.14 * (raio * raio)
       print("A área da circuferencia: {:.2f}".format(area))
    
    elif (opcao == 2):
        
        raio = float(input('Entre com o valor do raio, para obter o perimetro: '))
        perimetro = 2 * 3.14 * raio
        print("O perimetro da circuferencia é: {:.2f}".format(perimetro))
    