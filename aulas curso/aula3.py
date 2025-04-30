# tipo int e float
# int -> número inteiro
# o tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.

print(11) # int
print(-4) # int
print(0)

#float -> número com ponto flutuante
# o tipo float representa qualquer número + ou - com ponto flutuante
#float sem sinal = positivo

print(1.1, 10.12)
print(-14.0)
#print(-1.4.0) dá erro como se as () não tivessem
# sido fechadas.

#a função type mostra o tipo em python
# inferiu ao valor
print(  type('Yasmin')  )
print(  type(1.1), type(-1.1), type(0))

#boolean true ou false 
# o == questiona se um valor é igual a outro
print(10 == 10) #sim => True
print(10 == 11) #não => False

print(type(10 == 10)) #retorna classe => bool
