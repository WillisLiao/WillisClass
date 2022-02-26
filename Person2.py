#繳交readme格式在notion上(講要怎麼操作)，py檔也要交
from tkinter import *

class Person:
    def __init__(self, name, ID , height, weight, gender, address, email, phone ):
        self.name = name
        self.__ID = ID
        self.height = height
        self.weight = weight
        self.gender = gender
        self.address = address
        self.email = email
        self.__phone = phone
  
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name

    def setID(self, newID):
        self.__ID = newID
    def getID(self):
        return self.__ID

    def setHeight(self,newHeight):
        self.height = newHeight
    def getHeight(self):
        return self.height

    def setWeight(self,newWeight):
        self.weight = newWeight
    def getWeight(self):
        return self.weight

    def setGender(self, newGender):
        self.gender = newGender       
    def getGender(self):
        return self.gender

    def setAddress(self, newAddress):
        self.address = newAddress
    def getAddress(self):
        return self.address

    def setEmail(self, newEmail):
        self.email = newEmail
    def getEmail(self):
        return self.email    

    def setPhone(self, newPhone):
        self.__phone = newPhone
    def getPhone(self):
        return self.__phone  
    def StudentInfo(self):
       print(" name:{}\n ID:{}\n height:{}\n weight:{}\n gender:{}\n address:{}\n email:{}\n phone:{}".format(self.name, self.ID, self.height, self.weight, self.gender, self.birthday))
person1=Person(input(''), input(''), input(''), input(''), input(''), input(''), input(''), input('') )
class Student(Person):
    def __init__(self, name, ID, height, weight, gender, address, email, phone, subject, credit, score ):
        super().__init__(name, ID, height, weight, gender, address, email, phone, subject, credit, score)
        self.subject = subject
        self.credit = credit
        self.score = score
    def setSubject(self, newSubject):
        self.subject = newSubject
    def getSubject(self):
        return self.subject

    def setCredit(self, newCredit):
        self.credit = newCredit
    def getCredit(self):
        return self.credit

    def setScore(self, newScore):
        self.score = newScore
    def getScore(self):
        return self.score
    def ClassInfo(self):
        print("subject:{}\n credit:{}\n score:{}".format(self.subject, self.credit, self.score))

class Teacher(Person):
    def __init__(self, name, ID, height, weight, gender, address, email, phone, degree, major, web_address ):
        super().__init__(name, ID, height, weight, gender, address, email, phone, degree, major, web_address)
        self.degree = degree
        self.major = major
        self.web_address = web_address
root = Tk()
root.geometry('400x200')

entry1 = Entry(root, width = 20)
entry1.pack()




root.mainloop()


















    
 #   id = property(getID, setID)
#bd = property(getBirthday, setBirthday)
