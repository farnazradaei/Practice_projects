
class BankAccount :

    def __init__( self , balance : int = 0 ):
        self.__balance = balance
  
    def deposit( self , amount  ) ->int: 
       """
       this function takes two integers and
       return their 

       """    
       self.__balance += amount
    
    def withdraw( self , amount )->int:  
        """
        This function takes two integers and 
        returns their difference.
        raises ValueError: An error is raised if the value is negative or zero
        """ 
        if self.__balance - amount < 0 :
            raise ValueError("Insufficient funds!")

        else:
            self.__balance -= amount

    def get_balance(self)->int:
        return self.__balance    


        