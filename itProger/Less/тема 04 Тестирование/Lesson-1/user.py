class User:
    def __init__(self, name = "Bot", age = 35):
        self.name = name
        self.age = age

    def printAll(self):
        return "{} возрастом {}".format(self.name, str(self.age))

    def printToFile(self, fileName):
        file = open(fileName, "wt")
        file.write(self.printAll())
        file.close()

    def readFromFile(self, fileName):
        file = open(fileName, "rt")
        result = file.read()
        file.close()
        return result