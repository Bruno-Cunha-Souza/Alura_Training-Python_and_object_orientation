class Account:

    def __init__(self, holder, balance, limit):
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
    
    
    # Imprimir o saldo 
    def extract(self):
        print("{} o seu saldo é de: {}".format(self.__holder, self.__balance))
        
    # Deposito de saldo  
    def deposit(self, valor):
        self.__balance += valor 
        
    # Retirada de saldo
    def withdraw(self, valor):
        if(valor <= (self.__balance + self.__limit)):
            self.__balance-= valor
        else:
            print("O valor {} solicitado no saque utrapassa o seu saldo + o valor limite do seu imprestimo \n Seu saldo é de {} e seu limite {}".format(valor, self.__balance, self.__limit))
        
    # Tranferencia de saldo
    def transfer(self, valor, destination):
        self.withdraw(valor)
        destination.deposit(valor)
    
    # Mostrar saldo
    @property
    def balance(self):
        return self.__balance
    
    @property
    # Mostrar titular
    def holder(self):
        return self.__holder
    
    # Mostrar limite
    @property
    def limit(self):
        return self.__limit
    
   
    
    # Mudar limite
    @limit.setter
    def set_limit(self, limit):
        self.__limit = limit
        
    @staticmethod
    def bank_ID():
        return "001"
    