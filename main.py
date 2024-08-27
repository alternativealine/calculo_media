def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

def classificar_desempenho(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

notas_aluno = [6, 7, 8, 5, 9]
media = calcular_media(notas_aluno)
resultado = classificar_desempenho(media)

print(f"Média do aluno: {media:.2f}")
print(f"Desempenho: {resultado}")
