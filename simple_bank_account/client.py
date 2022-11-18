class Client:
    
    def __init__(self, name):
        self.__name = name  
    
    # Returna o nome do cliente
    @property
    def name(self):
        return self.__name.title()
    
    @name.setter
    def name (self, name):
        self.__name = name