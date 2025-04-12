class Person:
   """
   This class identifies a person by name and age.
   """
   def __init__(self, name: str, age: int):
       self.__name = name
       self.__age  = age
         
   def get_name(self):
       """
       Returns the person's name.
       """
       return self.__name
    
   def set_name(self, name: str):
       self.__name = name 

   def get_age(self):
       return self.__age
    
   def set_age(self, age: int):
       self.__age = age 


   def birthday(self):
       """
       Increases a person's age by one year.
       """
       self.__age += 1
       return self.__age
    

p = Person("Alice", 27)
p.birthday() 
print(p.get_age())