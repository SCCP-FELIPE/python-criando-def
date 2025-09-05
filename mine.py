def medidas():
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))
    comprimento = float(input("Digite o comprimento: "))
    return largura, altura, comprimento

def parede(largura, altura, comprimento):
    area_paredes = 2 * (largura * altura) + 2 * (comprimento * altura)
    print(f"Área total das paredes: {area_paredes:.2f} m²")

def teto(largura, comprimento):
    area_teto = largura * comprimento
    print(f"Área do teto: {area_teto:.2f} m²")


largura, altura, comprimento = medidas()
parede(largura, altura, comprimento)
teto(largura, comprimento)
