class Player:
    def __init__(self,id,name,strenght):
        self.id=id
        self.name=name
        self.strenght=strenght
    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def strenght(self):
        return self.strenght

    def __str__(self):
        return str(self.id)+','+str(self.name)+','+str(self.strenght)