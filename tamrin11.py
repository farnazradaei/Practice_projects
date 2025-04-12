import hashlib

class User:
    """
    A class to represent a user with authentication and password hashing.
    """
    def __init__(self, username: str, password: str):
        self.__username = username
        self.set_password(password)
       
    def get_username(self):
        return self.__username
    
    def set_username(self, username: str):
        self.__username = username

    def get_password(self):
        return self.__password
    
    def set_password(self, password: str):
        
        """
        Hashes the given password and stores it securely.

        """
        salt = "5gz"

        dataBase_password = password + salt
        hashed_password = hashlib.md5(dataBase_password.encode()) 
        self.__password = hashed_password.hexdigest()  
    
    def authenticate(self, username: str, password: str):
        """
        Validates the username and password against stored credentials.

        Args:
          username (str): The username entered by the user.
          password (str): The raw password entered by the user.

        Returns:
          bool: True if authentication is successful, False otherwise.

        """
        if username != self.__username:
            return False
       
        salt = "5gz"

        dataBase_password = password + salt
        hashed_password = hashlib.md5(dataBase_password.encode()).hexdigest()
        return hashed_password == self.__password


class AccountManager:
    """
    A class to manage multiple user accounts and authentication.

    Attributes:
        __users (list): A list of registered User objects.
    """
    def __init__(self):
        self.__users = []
    
    def add_user(self, user):
        self.__users.append(user)
    
    def check_password(self, username: str, password: str):
        for user in self.__users:
            if user.authenticate(username, password):
                return True
        return False


account_manager = AccountManager()
account_manager.add_user(User("Faezeh", "123456"))
account_manager.add_user(User("Fariborz", "ffborz"))
account_manager.add_user(User("Hamed", "kelaasor"))

print(account_manager.check_password("Faezeh", "1253456"))  
print(account_manager.check_password("Fariborz", "ffborz"))