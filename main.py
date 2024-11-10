# class cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def intro(self):
#         print ("hello i am a cat and my name is",self.name ,"and i am",self.age ,"years old")
#     def sound(self):
#         print("i make a meow sound")



# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def intro(self):
#         print ("hello i am a dog and my name is",self.name ,"and i am",self.age ,"years old")
#     def sound(self):
#         print("i make a woof sound")

# cat1=cat("pussy",4)
# dog1=dog("bunny",5)


# for animal in (cat1,dog1):
#     animal.intro()
#     animal.sounds()

#activity 2

class computer:
    def __init__(self):
        self.__maxprice=900
        
    def sell(self):
        print ("the selling price is",self.__maxprice)
    
    
    def setmaxprice(self,price):
        self.__maxprice=price

  

c=computer()
c.sell()

c.__maxprice=(1200)
c.sell()

c.setmaxprice(1200)
c.sell()
