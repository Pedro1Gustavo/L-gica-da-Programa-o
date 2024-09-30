total = 0
for i in range(5):   
    preco = float(input(f"Insira o preço do produto {i+1}: "))    
    total += preco   
    if total > 100:
        
        total *= 0.90  
        print(f"Total ultrapassou 100. Desconto aplicado. Novo total: {total:.2f}")
        break  
if total <= 100:
    print(f"Total dos produtos: {total:.2f}")