import CNPJ

cnpj = '04.252.011/0001-10'
cnpj = input("Digite um CNPJ: ")
        
if CNPJ.validateCNPJ (cnpj):
    print()
    print("CNPJ Válido")
    print()
else:
    print()
    print("CNPJ inválido")
    print()