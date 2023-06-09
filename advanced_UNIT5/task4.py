# todo: Magic methods.
# Description
# You have to implement class Book with attributes price, author, name.
# author and name fields have to be immutable;
# price field may be changes but has to be in 0 <= price <= 100 range.
# If user tries to change author or name fields after initialization or set price out of range, the ValueError should be raised.
#
# Implement descriptors PriceControl and NameControl to validate parameters.
#
# Example
# >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
# >>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Author='William Faulkner', Name='The Sound and the Fury', Price='12'
#
# >>> b.price = 55
# >>> b.price
# 55
# >>> b.price = -12  # => ValueError: Price must be between 0 and 100.
# >>> b.price = 101  # => ValueError: Price must be between 0 and 100.
#
# >>> b.author = "new author"  # => ValueError: Author can not be changed.
# >>> b.name = "new name"      # => ValueError: Name can not be changed.
#
# Шаблон:

class PriceValidator:
    __value = 0

    def __init__(self, value):
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):

        if 0 <= value <= 100:
            self.__value = value
        else:
            raise ValueError("Price must be between 0 and 100")
        
    def __str__(self):
        return f"{self.__value}"

class NameValidator:
    __value = ""
    __name = ""

    def __init__(self, value: str, name: str):
        self.__value = value
        self.__name = name

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: str):
        raise ValueError(f"{self.__name} can not be changed")
        
    def __str__(self):
        return f"{self.__value}"
        

class Book:
    __author: NameValidator
    __title: NameValidator
    __price: PriceValidator

    def __init__(self, author: str, name: str, price: int):
        self.__author = NameValidator(author, "Author")
        self.__title = NameValidator(name, "Name")
        self.__price = PriceValidator(price)

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value: str):
        self.__author.value = value

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value: str):
        self.__title.value = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price.value = value


b = Book("Омар Хайям", "Рубаи", 18)

print(f"Author='{b.author}', Name='{b.title}', Price='{b.price}'")

b.price = 99.99

print(f"Author='{b.author}', Name='{b.title}', Price='{b.price}'")