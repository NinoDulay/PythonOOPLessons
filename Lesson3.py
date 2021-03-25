#Encapsulation

# Nagtatago tayo ng attributes para hindi magalaw ng mga user
class Account:
    def __init__(self, username, password):
        #Public attributes
        # self.username = username
        # self.password = password

        #Gagamit lang ng encapsulation, kapag need magtago ng mga attribute
        #Private attributes (dapat laging private attribute kapag nageencapsulate)
        # to create a private variable, you need to add two underscores before the name of the variable
        self.__username = username
        self.__password = password

    #parameter
    def login(self, username, password):
        pass

    def logout(self):
        pass

    ############################################################__username

    #Getters - lahat ng private attribute is dapat merong getter
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password

    ############################################################

    #Setters - naglalagay tayo ng restriction  
    def set_username(self, new_username):
        if len(new_username) >= 5:
            self.__username = new_username
        else:
            print("Username must be 5 characters and above")

    def set_password(self, currentPassword, newPassword):
        if currentPassword == self.__password:
            self.__password = newPassword

#Instantiation
account1 = Account("Nino123", "Password123")


#Example (Itatry natin na iset yung private variable and then use the getter)
account1.__username = "Nino12345"
print(account1.get_username())

account1.__password = "Password12345"
print(account1.get_password())

print()

#Getters
print(account1.get_username())
print(account1.get_password())

print()

#Setters
#Set the username and then print it
# account1.set_username("Nino") #This wont work because it is only 4 characters
account1.set_username("NinoDulay10")
print(account1.get_username())

#Set the password and then print it
account1.set_password("Password12", "password12345")
#account1.set_password("Password123", "password12345")
print(account1.get_password())