
soma_notas = 0

for i in range(5):
    
    nota = float(input(f"Digite a nota {i + 1}: "))
    
    soma_notas += nota

media = soma_notas / 5

if media >= 6:
    classificacao = "Aprovado"
else:
    classificacao = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")