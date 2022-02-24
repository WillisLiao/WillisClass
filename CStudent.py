class CStudent:
    def __init__(self, ID, name, department, Email, birthday):
        self.name = name
        self.__ID = ID
        self.department = department
        self.Email = Email
        self.__birthday = birthday
    

    @property
    def name(self):
        return "No Data"
    @name.setter
    def setName(self, newName):
        self.name = newName
    @name.getter
    def getName(self):
        return self.name


    @property
    def ID(self):
        return "No Data"
    @ID.setter
    def setID(self, newID):
        self.__ID = newID
    @ID.getter
    def getID(self):
        return self.__ID

    @property
    def department(self):
        return "No Data"
    @department.setter
    def setDepartment(self,newDepartment):
        self.department = newDepartment
    @department.getter
    def getDepartment(self):
        return self.department

    @property
    def Email(self):
        return "No Data"
    @Email.setter
    def setEmail(self,newEmail):
        self.Email = newEmail
    @Email.getter
    def getEmail(self):
        return self.Email


    @property
    def birthday(self):
        return "No Data"
    @birthday.setter
    def setBirthday(self, newBirthday):
        self.__birthday = newBirthday     
    @birthday.getter  
    def getBirthday(self):
        return self.__birthday

  
        
    @property    
    def showInfo(self):
       print(" ID:{}\n name:{}\n department:{}\n Email:{}\n birthday:{}".format(self.__ID, self.name, self.department, self.Email, self.__birthday))
    

    
    id = property(getID, setID)
    bd = property(getBirthday, setBirthday)

    @staticmethod
    def objCountAdd():
        CStudent.objCount +=1

    @staticmethod
    def getObjCount():
        return CStudent.objCount
