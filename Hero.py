class Hero:
    def __init__(self, name, hp , height, weight, gender ):
        self.name = name
        self.hp = hp
        self.height = height
        self.weight = weight
        self.gender = gender
  
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return print(self.name)

    def setHp(self, newHp):
        self.hp = newHp
    def getHp(self):
        return print(self.hp)

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
        
        
    def showInfo(self):
       print(" name:{}\t hp:{}\t height:{}\t weight:{}\t gender:{}\t".format(self.name, self.hp, self.height, self.weight, self.gender))
    

hero1 = Hero('Willis', '60000','186', '69', 'male')   #對應上面的參數，self不用
hero2 = Hero('XMY', '9999','186', '69', 'male') 
hero3 = Hero('JimCarrey', '9562','186', '69', 'male') 
hero1.showInfo()
hero2.showInfo()
hero3.showInfo()

