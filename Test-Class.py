class person:
    def __init__(self, name, age, sex):
        print(" Open class person")
        self.name, self.age, self.sex = name, age, sex
    def getName(self):
        print("Name : " , self.name)
    def getAge(self):
        print("Age : " , self.age)
    def getSex(self):
        print("Sex :" , self.sex)
    def __del__(self):
        print("Xoa Class")

person = person("Bao", 22, "Male")
person.getName()
person.getAge()
person.getSex()



