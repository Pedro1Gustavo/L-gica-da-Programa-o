texto = (input("Digite uma palavra:"))
contador_vogais = 0 
for caractere in texto:
    if caractere.lower() in "aeiou":
       contador_vogais += 1
print(f"Número de vogais: {contador_vogais}")