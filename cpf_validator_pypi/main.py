from cpf_and_cnpj import Documento


ex = "35379838000112"

# cnpj = CNPJ()
# print(cnpj.validate(ex_cnpj))

# cpf = "15316264754"
# objeto_cpf = CpfCnpj(cpf)
# print("\n---------------")
# print(objeto_cpf)
# print("---------------\n")

documento = Documento.cria_doc(ex)

print("\n||------------------||")
print(" ", documento, "") 
print("||------------------||\n")

