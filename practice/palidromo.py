def isPalindrome(x: int) -> bool:
    xInStr = str(x)
    lastIndex = len(xInStr)-1
    i = 0
    reverseInfo = ""
    while i <= lastIndex:
        reverseInfo = reverseInfo + xInStr[lastIndex - i]
        #code here
        i +=  1
    return reverseInfo == xInStr
result = isPalindrome(1241)
print(result)

#solução em um alinha
#xInStr = str(x)
#return xInStr[::-1] == xInStr