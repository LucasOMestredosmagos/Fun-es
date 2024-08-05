def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10"
    else:
        return "Aprovado"

notas = []
while True:
    nota = input("Digite uma nota (ou 'sair' para finalizar): ")
    if nota.lower() == "sair":
        break
    notas.append(float(nota))

media = calcular_media(notas)
print(f"Média: {media:.2f}")
print(verificar_situacao(media))