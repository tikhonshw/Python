class Some:
    name = "John"
    number = 20

    def __add__(self, str):
        print("Some " + str)

    # def __new__(self):
    #     self.__add__(self, "new")
    #     self.__init__(self)

    def __init__(self):
        print("Init started")
    def __str__(self):
        return "Name: " + self.name
    def __ge__(self, x):
        if(self.number >= x):
            return True
        else:
            return False
    def __le__(self, x):
        if(self.number <= x):
            return True
        else:
            return False

    def __del__(self):
        print("Delete object")

obj = Some()
obj + "new"
print(obj <= 50)
print(dir(obj))
