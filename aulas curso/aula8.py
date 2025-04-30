nome = 'Yasmin'
altura = 1.60
peso = 54
imc = peso / (altura * altura) # ou peso / altura **2
print ('Resultado:',imc)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos, e seu imc é'
linha_3 = f'{imc:.2f}' #2 casas decimais

print(linha_1)
print(linha_2)
print(linha_3)