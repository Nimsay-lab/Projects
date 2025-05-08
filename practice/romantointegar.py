s= 'MCMXCIV'
romanValues={
    'CM':900,
    'M': 1000,
    'CD':400,
    'D': 500,
    'XC': 90,
    'C':100,
    'XL':40,
    'L':50,
    'IX':9,
    'X':10,
    'IV':4,
    'V':5,
    'I':1
}

i = 0 
accumalator = 0 
while i < len(s):
    if(i != len(s) - 1):
        compounNumber = s[i] + s[i+1]
        if(romanValues.get(compounNumber) != None):  #compounNumber = compound 
            accumalator = accumalator + romanValues[compounNumber] # this line is accumulating single numbers
            i = i + 2
            continue
    accumalator = accumalator + romanValues[s[i]]
    i = i + 1

print(accumalator)

# search other answers online