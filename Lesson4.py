#Aggregation - has a 
#Composition - part of

#Kotse - gulong
## Class kotse, class na gulong
#Aggregation

#Tao - kamay
## Class human, class na kamay
#Composition


#Aggregation

class Car:
    def __init__(self, wheel1, wheel2, wheel3, wheel4):
        self.wheels = [wheel1, wheel2, wheel3, wheel4]

class Wheel:
    def __init__(self, brand):
        self.brand = brand

w1 = Wheel("Ferrari")
w2 = Wheel("Ferrari")
w3 = Wheel("Ferrari")
w4 = Wheel("Ferrari")

#car1 = Car(w1,w2,w3,w4)

#Composition
class Hand:
    def __init__(self, finger):
        self.finger = finger

class Human:
    def __init__(self):
        self.leftHand = Hand(5)
        self.rightHand = Hand(5)

human1 = Human()

###################################################
class Account:  
    def __init__(self, username, age, password):
        self.username = username
        self.age = age
        self.__password = password

    def login(self):
        username = input("Enter your name: ")
        password = input("Enter your password: ")
        confirmPassword = input("Enter your password again: ")
        if username == self.username:
            if password == self.__password and password == confirmPassword:
                print("You are now logged in")
            else:
                print("You entered the wrong password")
        else:
            print("You entered the wrong username")



class Computer:
    def mainMenu(self):
        while True:
            print("What do you want to do: ")
            print("a. Login")
            print("b. Shutdown Computer")
            print("c. Restart Computer")

            userChoice = input("Enter the letter you want to choose: ")
            if userChoice.upper() == "A":
                acc1 = Account("John Jay", 26, "Password")
                acc1.login()
                break
            elif userChoice.upper() == "B":
                quit()
            elif userChoice.upper() == "C":
                print("Restarting computer.. please wait..")
                self.mainMenu()
            else:
                print("Wrong letter, please only enter a,b, or c")
comp1 = Computer()
comp1.mainMenu()


# while condition

#Condition = Boolean

# Operational conditions (Logical)
'''
==
<=
>=
>
<
and
or
not
'''
# "a" == "a" #true
# "a" == "A" #false
# 5 == 5 #true
# 5 <= 5 #true
# 5 < 5 #false
# True or True #true

# #Kapag 'or' ang gamit, kahit isa lang sa dalawang condition ang need na true
# False or True #true

# False or False #False

# # 'and', dapat lahat is True
# True and True #True
# True and False #False
# False and True #False

# not(True) #False
# not(False) #True

