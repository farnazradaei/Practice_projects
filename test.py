class User:
    id = 0

    def __init__(self, username: str, password: str , email : str ):
        self.__username = username
        self.set_password(password)
        self.id=User.id
        User.id += 1


    def get_username(self):
        return self.__username
    @staticmethod
    def set_username( username: str):
        return username

    def get_password(self):
        return self.__password
    
    def get_email(self):
        return 
    
    @staticmethod
    def check_email(email : str):
        email_

    @property

    