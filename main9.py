for num in range(1, 21): 
    if num == 15:
        print("Encontramos o número 15. Parando o loop.")
        break
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")