class Book:
    def __init__(self, book_id, title, author):
        self.__book_id =  book_id
        self.__title = title
        self.__author = author

    @property
    def book_id(self):
        return self.__book_id
    
    # @book_id.setter
    # def book_id(self, new_value):
    #     self.__book_id = new_value
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_value):
        self.__title = new_value
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, new_value):
        self.__author = new_value

    def __str__(self):
        return f"{self.book_id}. {self.title} by {self.author}"