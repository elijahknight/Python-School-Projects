import re
import datetime
class Person:
    def __init__(fName,lName,Addr,DOB,email,SSN,uName,pWord,pNum):
        self.firstName = fName
        self.lastName = lName
        self.address = Addr
        self.birthdate = DOB
        self.Email = email
        self.SocialNum = SSN
        self.userName = uName
        self.password = pWord
        self.phoneNum = pNum

    def setFName(self,firstName):
        self.firstName = firstName

    def setLName(self,lastName):
        self.lastName = lastName

    def setAddr(self,address):
        self.address = address

    def setDOB(self,birthdate):
        if validateDOB(birthdate):
            self.birthdate = birthdate

    def setEMail(self,Email):
        if validateEmail(Email):
            self.Email = Email
                

    def setSocialNum(self,SocialNum):
        if validateSSN(SocialNum):
            self.SocialNum = SocialNum

    def setUName(self,userName):
        self.userName = userName

    def setPWord(self,password):
        if validatePWord(password):
            self.password = password

    def setPNum(self,phoneNum):
        if validatePNum(phoneNum):
            self.phoneNum = phoneNum

    def getName(self):
        return self.firstName + self.lastName

    def getAddr(self):
        return self.address

    def getDOB(self):
        return self.birthdate

    def getEMail(self):
        return self.Email

    def getSocialNum(self):
        return self.SocialNum

    def getUName(self):
        return self.userName

    def getPWord(self):
        return self.password

    def getPNum(self):
        return self.phoneNum

    def validateEmail(self):
        eAddress = self.Email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',eAddress)
        if match == None:
            print('not a valid email address')
            return false
        else:
            return true

    def validateDOB(self):
        DoB = self.birthdate
        try:
            birthdate = datetime.datetime.strptime(dob, "%d/%m/%Y")
        except:
            print("Not a valid date of birth")

    def validateSSN(self):
        ssn = self.SocialNum
        if len(ssn) == ssn[0:3] and ssn[5:6] and ssn[8:11] == ssn.isdigit():
            if len(ssn) == ssn[4 and 7] == "-":
                print("Your Social Security is valid")
            else:
                print("Your Social Security is invalid")
                return false

    def validatePWord(self):
        while True:
        pword = self.password
        if len(pword) < 7:
            print("Make sure your password is at lest 7 characters")
        elif re.search('[0-9]',pword) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',pword) is None: 
            print("Make sure your password has a capital letter in it")
        elif re.search('[!@#$%^&*(),.?":{}|<>]',pword) is None:
            print("Make sure your password has a special character in it")
        else:
            print("Your password is valid")
        break

    def validatePNum(self):
        while True:
        pnum = self.phoneNum
        if len(pnum) == 10 and pnum.isdigit():
            if len(pnum) == pnum[4 and 8] == "-":
                print("valid phone number")
            else:
                print("invalid phone number")


class Address:
    def __init__(L1, L2, city, state, pCode, country):
        self.line1 = L1
        self.line2 = L2
        self.City = city
        self.State = state
        self.postCode = pCode
        self.Country = country

    def setL1(self, line1):
        self.line1 = line1

    def setL2(self, line2):
        self.line2 = line2

    def setCity(self, City):
        self.City = City

    def setState(self, State):
        self.State = State

    def setPost(self, postCode):
        if validatePost(postCode):
            self.postCode = postCode

    def setCountry(self, Country):
        self.Country = Country

    def getL1(self):
        return self.line1

    def getL2(self):
        return self.line2

    def getCity(self):
        return self.City

    def getState(self):
        return self.State

    def getPost(self):
        return self.postCode

    def getCountry(self):
        return self.Country

    def getAddress(self):
        return [self.line1 + ' ' + self.line2 + ' ' + self.City + ', ' + self.State + ' ' + self.postCode + ' ' + self.Country]

    def validatePost(self, postCode):
        pc = self.postCode
        if len(pc) = 5 and pc.isdigit():
            return true
        else:
            print('not a valid postal code')
            return false

class Employee(Person):
    def __init__(identification, start, end, title, supervisor, vDays, uVDays):
        self.ID = identification
        self.sDate = start
        self.eDate = end
        self.Title = title
        self.Supervisor = supervisor
        self.vacaDays = vDays
        self.usedDays = uVDays

    def setID(self, ID):
        self.ID = ID

    def setStart(self, sDate):
        if validateSDate(sDate):
            self.sDate = sDate

    def setEnd(self, eDate):
        if validateEDate(eDate):
            self.eDate = eDate

    def setTitle(self, Title):
        self.Title = Title

    def setSupervisor(self, Supervisor):
        self.Supervisor = Supervisor

    def setVDays(self, vacaDays):
        if validateVDays(vacaDays):
            self.vacaDays = vacaDays

    def setUDays(self, usedDays):
        self.usedDays = usedDays

    def getID(self):
        return self.ID

    def getStart(self):
        return self.sDate

    def getEnd(self):
        return self.eDate

    def getTitle(self):
        return self.Title

    def getSupervisor(self):
        return self.Supervisor

    def getVDays(self):
        return self.vacaDays

    def getUDays(self):
        return self.usedDays

    def validateSDate(self):
        SD = self.sDate
        try:
            sDate = datetime.datetime.strptime(SD, "%d/%m/%Y")
        except:
            print("Not a valid date")

    def validateEDate(self):
        ED = self.eDate
        try:
            eDate = datetime.datetime.strptime(ED, "%d/%m/%Y")
        except:
            print("Not a valid date")

    def getDaysWorked(self):
        if self.eDate = none:
            days = datetime.datetime.now().date() - self.sDate
        else:
            days = self.eDate - self.sDate
        return days
    
    def validateVDays(self):
        vdays = self.vacaDays
        udays = self.usedDays
        if vdays.isdigit():
            return true
        else:
            print('not a valid number of days')
            if edays.isdigit():
                return true
            else:
                print('not a valid number of days')

    def showAvailableVDays(self):
        vdays = self.vacaDays
        udays = self.usedDays
        available = vdays - uday
        return available


class Customer(Person):
    def __init__(eDate, tDate, shipAddr, altCon, oDate):
        self.effDate = eDate
        self.termDate = tDate
        self.shipAdd = shipAddr
        self.altContact = altCon
        self.orderDate = oDate

    def validateEffDate(self):
        date = self.effDate
        try:
            effDate = datetime.datetime.strptime(date, "%d/%m/%Y")
        except:
            print("Not a valid date")

    

    def validatetermDate(self):
        td = self.termDate
        try:
            termDate = datetime.datetime.strptime(td, "%d/%m/%Y")
        except:
            print("Not a valid date")

    def validateOrderDate(self):
        od = self.orderDate
        try:
            orderDate = datetime.datetime.strptime(od, "%d/%m/%Y")
        except:
            print("Not a valid date")


def createPeople():
    employee = Employee('John', 7/4/1998, 12/30/18, 'cashier', 'Mark', 12, 4)
    customer = Customer(4/8/18, 4/9/18, 'WV, USA', 3046220987, 4/1/18)
    employeeAddr = Address('222', 'Wood Ave', 'Wheeling', 'WV', '26003', 'USA')
    customerAddr = Address('223', 'Maple Ave', 'Wheeling', 'WV', '26003', 'USA')


    
    
            
    
        
            
    
    


    


                
            

    

    

    

    
        

    
    
