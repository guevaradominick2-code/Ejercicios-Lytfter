from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name): 
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    
    def get_role(self):
        return "admin"
    
    def has_permission(self, permission):
        return True

class RegularUser(User): 
    
    def get_role(self):
        return "regular"
    
    def has_permission(self, permission):
        return permission.lower() in ["read","edit"]

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete")) 
print(user2.has_permission("delete"))   
print(user2.has_permission("read"))  
print(user2.has_permission("READ"))     
print(user2.has_permission("Edit"))    
print(user1.get_role())                 
print(user2.get_role())     