def validateCNPJ (cnpj):
    
    cnpj = removeChar (cnpj)
    
    try:
        if isSequence (cnpj):
            return False
    except IndexError: 
        return False
    
    try:
        newCNPJ = bildLastDigit(cnpj=cnpj, removePrimareDigit=True) # Obtendo o penúltimo dígito verdadeiro do CNPJ
        newCNPJ = bildLastDigit(cnpj=newCNPJ, removePrimareDigit=False) # Obtendo o último dígito verdadeiro do CNPJ
    except IndexError:
        return False
    
    return True if cnpj == newCNPJ else False
    
def removeChar (cnpj):
    import re
    return re.sub(r'[^0-9]', '', cnpj) # removendo as pontuações

def isSequence (cnpj):
    result = cnpj[0] * len(cnpj) # verificando se é sequência
    return True if result == cnpj else False

def bildLastDigit(cnpj, removePrimareDigit):
    
    REGRESSIVE = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    newCNPJ = cnpj
    
    if removePrimareDigit == True:
        REGRESSIVE = REGRESSIVE[1:] 
        newCNPJ = cnpj[:-2] 
    else:
        REGRESSIVE = REGRESSIVE
    
    sum = 0
    digit = 0
    
    for index, regress in enumerate(REGRESSIVE):
        sum += int(newCNPJ[index]) * regress # multiplicando em ordem regressiva

    digit = 0 if (11 - (sum % 11)) > 9 else (11 - (sum % 11)) # validando o dígito gerado
    return newCNPJ+str(digit)