class Computer:
    def __init__(self):
        self.__max__price=10000
    def sell(self):
        print("Selling Price of Computer is",self.__max__price) 
    def setmaxprice(self,price):
        self.__max__price=price

comp1=Computer()  
comp1.sell()

comp1.__max__price=20000
comp1.sell()

comp1.setmaxprice(20000)
comp1.sell()
        