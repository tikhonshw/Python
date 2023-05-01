class Car:
    __color = ""
    weight = 0

    def set(self, color, weight):
        self.__color = color
        self.weight = weight

class BMW (Car):
    isM_model = False

    def set(self, color, weight, isM_model):
        self._Car__color = color
        self.weight = weight
        self.isM_model = isM_model

class Mercedes (Car):
    isMaybach = False

x3 = BMW()
x3.set("Белый", 2400, False)
print(x3._Car__color)

m3 = BMW()
m3.set("Синий", 1400, True)
print(m3.isM_model)
