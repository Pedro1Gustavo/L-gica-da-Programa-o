contagem_positivos = 0
contagem_negativos = 0
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))  

    
    if numero > 0:
        contagem_positivos += 1  
    elif numero < 0:
        contagem_negativos += 1  
print(f"Números positivos: {contagem_positivos}")
print(f"Números negativos: {contagem_negativos}")