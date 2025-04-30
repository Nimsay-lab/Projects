

#secondValue = int( input('type the second value:'))

exampleArray = [1,2,3,4]
for value in exampleArray:
    print(value)
operation =''
accumulator = int(input("digite um número: "))
# o valor de accumulator não está sendo atualizado
while operation != 'x':
    operation = input("Digite uma operação:")
    if operation == 'x':
        break
    # break ends loop
    operationValidationAdd = operation == '+'
    print(operationValidationAdd)
    value2 = int(input("digite outro número: "))
    result = 0
    if operationValidationAdd:
        result = accumulator + value2
        print('we are adding')

    if operation == '-':
        print('we are subtracting')
        result = accumulator - value2 
    if operation == '/' :
        print('we are dividing')
        result = accumulator / value2
    if operation == '*':
        print('we are multiplying')
        result = accumulator * value2
    print(result)
    accumulator = result
print('Operations Ended!')
# como parar a calculadora depois do resultado de cada operação?
# como adicionar mais de uma operação juntas?