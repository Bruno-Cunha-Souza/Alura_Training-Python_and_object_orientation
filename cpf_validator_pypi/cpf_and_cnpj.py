from validate_docbr import CPF, CNPJ

#Class Principal que verifica a entrada e chama suas respectivas funções
class Documento:
    #Metodo imutavel
    @staticmethod
    def cria_doc(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos informados esta incorreto")
        
#Classe para entrada de documentos tipo CPF        
class DocCpf:
    
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError ("CPF Invalido")
    
    def __str__(self):
        return self.format()
    
    def valida(self, documentos):
        validador = CPF()
        return validador.validate(documentos)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
#Classe para entrada de documentos tipo CNPJ
class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError ("CNPJ Invalido")
        
    def __str__(self):
        return self.format() 
    
    def valida(self, documento):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
 