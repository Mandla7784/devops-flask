
class User:

    def __init__(self, name , email):
        self.name = name
        self.email = email
        
    def signUp(name , email):
        
        if name ==None:
            return NameError("name canot be null value")
        else:
            print(name , email)
        
    def getName(self):
        
        return self.name
    
        
    def getEmail(self):
        return self.email
        

newUser = User("king","efgsvafD")
print( "The Users Name is : " , newUser.getName())
