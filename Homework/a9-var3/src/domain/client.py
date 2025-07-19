class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name
    
    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_value):
        self.__name = new_value
    
    def __str__(self):
        return f"{self.client_id} -> {self.name}"

   

