# A static attribute, sometimes called a (class attribute) is an attribute 
# that belongs to the class itself, not to any specific instance of the class/specific object created from the class.

# Meaning that static attributes are shared by all instances or objects of a class.
# One copy of a static attribute in memory irregardless of how many objs or instances you create from the class. 

# Static attributes can be accessed directly through the class itself and also through the instances
# although they are stored at the class level.


class User:
    user_count=0 # static attribute # Exists on class, not on objects created from the class
                 # Stored in one place on the class, not uniquely on each object.
                 # Created only once at class level and are shared between the class it resides in and instance objects of that class.

    def __init__(self, username, email): # init method 
        self.username=username # instance attribute # Created everytime we create a new instance (User(......)) # Contained within each unique object (user1, user2)
        self.email=email # Storing object specific data
        User.user_count +=1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user1=User("spiderman","peterparker@gmail.com")
user2=User("ironman","tonystark@gmail.com")

print(User.user_count) # Accessed Directly by Class(User).attribute_name
print(user1.user_count) # Can also accessed by instance created from the class (user1)
print(user2.user_count)

# When to use?

#-->Static attributes are useful for data that is common to all instances of a class.
# Example: Counters and totals (Tracking)
# Example: Shared constants, default values applicable across all instances. 
# Configurating setting in class, same setting for all instance of a class such as default parameters. 