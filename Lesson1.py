#Lesson 1: Classes, Constructor, Attributes, Methods

#Object Oriented Programming is naglalaman ng mga Classes, Methods(Function), Attributes(Variable)


# Tinatawag na Method ang isang function, kapag nasa loob ng class ang isang function

# Tinatawag na attribute ang isang variable, kapag nasa loob ng isang class.

# name = "Brownie"
# age = 5
# color = "Brown"

# def bark():
#     print("Arf arf!")

# name = "Nino"
# age = 17



# Ang class ay isang object
# Ang object/class ay binubuo ng sama samang function at variable
#########################################
#Simplest example of a class
#Class/Object
# class Dog:  
#     name = "Brownie"
#     age = 5
#     color = "Brown"

#     def bark():
#         print("Arf arf!")
# #Class.name  /  Class.age


# class Dog2:
#     name = "Cheesecake"
#     age = 4
#     color = "White"

#     def bark():
#         print("Bark bark!")

# print(Dog.name)
# print(Dog2.name)

#############################################

# class Dog:
#     pass

# # Instantiate/Gagawa ng bagong object
# dog1 = Dog()
# dog2 = Dog()

# dog1.name = "Brownie"
# dog2.name = "Cheesecake"
# print(dog2.name)

##########################################

#Constructor - siya yung function na gumagana kapag gumagawa tayo ng object
# class Person:
#     #Constructor
#     def __init__(self):
#         print("A person has been created")

#To create a object, use this format: variableName = Class()


# Ang isang class ay pwedeng maging blueprint
#class Name: Dog
class Dog:
    #self dapat lagi ang unang parameter ni __init__
    def __init__(self, name, age, color, ears):
        #Attributes/Variable
        # Katangian
        self.name = name
        self.age = age
        self.color = color
        self.ears = ears
    
    #Ugali/Ginagawa
    #Method - ang lahat ng method ng isang class ay dapat ang unang parameter ay self
    def bark(self):
        return "Arf arf!"
    def walk(self):
        print("Walking...")
    def sleep(self):
        print("Sleeping...")

#To create a object
#FORMAT/FLOW: ClassName(attribute1, attribute2, attribute3, ..... and so on)

dog = Dog("Brownie", 5, "Brown", 2)
print(dog.name)






#######################
# Return vs Print


# def add(x, y):
#     print(x + y)
#value1 = add(5,5)
#print(value1)

# #Ang mga function na may return, pwedeng ilagay sa variable
# def addWithReturn(x, y):
#     return x + y


# #value2 = addWithReturn(10,10)

# print(addWithReturn(10,10))