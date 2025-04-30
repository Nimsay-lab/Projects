numberArray = [1,2,3,4,5]

stringArray = ["teste1", "teste2", "teste3", "teste4"]
print(stringArray)
print(stringArray[0])
# index = "[]"access a specific part of a array
numerDictionary = {
    'yasmin': 21,
    'gustavo': 25
}

print(numerDictionary['yasmin'])

operationArray = [{
    'firstValueName':'firstAdditor',
    'secondValue': 'secondAdditor',
    'symbol': '+'
},{
    'firstValueName':'firstSubtractor',
    'secondValue': 'secondSubtractor',
    'symbol': '-'
},{
    'firstValueName':'firstMultiplier',
    'secondValue': 'secondMultiplier',
    'symbol': '*'
},{
    'firstValueName':'firstDivisor',
    'secondValue': 'secondDivisor',
    'symbol': '/'
}]


optionSelection = int(input("choose a operation:") )
print(optionSelection)

print("please tyoe your" + operationArray[optionSelection]['firstValueName'])
print("please tyoe your" + operationArray[optionSelection]['secondValue'])