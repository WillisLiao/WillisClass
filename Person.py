class Person:
    def __init__(self, name, ID , height, weight, gender, birthday ):
        self.name = name
        self.__ID = ID
        self.height = height
        self.weight = weight
        self.gender = gender
        self.__birthday = birthday
  
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return print(self.name)

    def __setID(self, newID):
        self.__ID = newID
    def getID(self):
        return print(self.__ID)

    def setHeight(self,newHeight):
        self.height = newHeight
    def getHeight(self):
        return print(self.height)

    def setWeight(self,newWeight):
        self.weight = newWeight
    def getWeight(self):
        return print(self.weight)

    def setGender(self, newGender):
        self.gender = newGender       
    def getGender(self):
        return print(self.gender)

    def __setBirthday(self, newBirthday):
        self.__birthday = newBirthday
    def getBirthday(self):
        return print(self.__birthday)
        
        
    def showInfo(self):
       print(" name:{}\n ID:{}\n height:{}\n weight:{}\n gender:{}\n birthday:{}".format(self.name, self.__ID, self.height, self.weight, self.gender, self.__birthday))
    def getStdBMI(self):
        print("BMI:",int(self.weight)/((int(self.height)*(0.01))**2))

person1 = Person('Willis', 'F130374671','186', '69', 'male','0414')   #對應上面的參數，self不用

person1.showInfo()
person1.getStdBMI()
person1.setGender('Gorilla')
person1.getGender()
person1.setBirthday('0918')
person1.getBirthday()
