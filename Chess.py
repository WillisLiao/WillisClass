class Chess:
    def __init__(self, name, mass , color, value, startingPosi ):
        self.name = name
        self.mass = mass
        self.color = color
        self.value = value
        self.startingPosi = startingPosi
  
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return print(self.name)

    def setMass(self, newMass):
        self.mass = newMass
    def getMass(self):
        return print(self.mass)

    def setColor(self,newColor):
        self.color = newColor
    def getColor(self):
        return print(self.color)

    def setValue(self,newValue):
        self.value = newValue
    def getValue(self):
        return print(self.value)

    def setStartingPosi(self, newStartingPosi):
        self.startingPosi = newStartingPosi       
    def getStartingPosi(self):
        return print(self.startingPosi)
        
        
    def showInfo(self):
       print(" name:{}\t mass:{}\t color:{}\t value:{}\t startingPosition:{}\t".format(self.name, self.mass, self.color, self.value, self.startingPosi))
    

chess1 = Chess('king', '16g','white', '10', 'e1')   #對應上面的參數，self不用
chess2 = Chess('rook', '15g','black', '7', 'a8, h8') 
chess3 = Chess('knight', '15g','white', '5', 'b1, g1') 
chess1.showInfo()
chess2.showInfo()
chess3.showInfo()

