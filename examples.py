def test1234():
    return 1 + 2

print(test1234())

class Person1  () :
 def getName ()  :
                return "John Doe"
 



class Company:
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name

class User:
    def __init__(self, name: str, salary: int = 123):
        self._name = name
        self._salary = salary

    def name(self) -> str:
        return self._name

    def salary(self) -> int:
        return self._salary

company = Company("binary stars")
company = None 
user = User("John Doe")
user = None 
user = User("John Doe", 123_000)

type = ("default" if company == None else f"{company.name()} employee") if user == None else "staff" if user.salary() < 100_000 else "manager"
print(type)


roleByCompany = lambda: "default" if company == None else f"{company.name()} employee"
roleBySalary = lambda: "staff" if user.salary() < 100_000 else "manager"
if user == None:
    type = roleByCompany()
else:
    type = roleBySalary()
print(type)


class Person:    
  

  def getFirstName(self) -> str:



    return "Joey"  
  def getLastName(self) -> str:
    return "Ramone"
  



class Person3:      
  
  def getFirstName(self) -> str:
    return "Joey"  
  
  def getLastName(self) -> str:
    return "Ramone"

person = Person()
print(f"{person.getFirstName()} {person.getLastName()}")

import math
class Circle1:

  def __diameter(self) -> float:
    return self.radius * 2

  def area(self) -> float:
    return self.__diameter() * math.pi
  

  def __init__(self, radius: float):
    self.radius = radius

circle = Circle1(5.0)
print(f"Circle with radius {circle.radius} has area {circle.area()} ")


class Circle2:
  def __init__(self, radius: float):
    self.radius = radius

  def area(self) -> float:
    return self.__diameter() * math.pi
  
  def __diameter(self) -> float:
    return self.radius * 2



circle = Circle2(2.0)
print(f"Circle with radius {circle.radius} has area {circle.area()} ")


class Salary:
    def __init__(self, cents: int = 0, currency: str = "EUR"):
        self.cents = cents
        self.currency = currency

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"
    
class UserWithSalary:
    def __init__(self, name: str, salary: Salary = Salary()):
        self._name = name
        self._salary = salary

    def name(self) -> str:
        return self._name

    def setSalary(self, salary: Salary):
        self._salary = salary

    def salary(self) -> Salary:
        return self._salary
    
user = UserWithSalary("John Doe")
    
# get the user's salary as float in EUR
salary = Salary()
salary.cents = 3216
salary.currency = "USD"
user.setSalary(salary)

s1 = "a"
s2 = "b"
s3 = "c"
s = "{} {} {}".format(s1, s2, s3)
print(s)

salutation = "a"
firstName = "b"
lastName = "c"
addressLine1 = "{} {} {}".format(salutation, firstName, lastName)
print(addressLine1)
#self.printer.printAddressLine(addressLine1)


class ControllerForValidationOfStrings:
   pass

class ControllerForStorageOfStrings:
   pass

class NumberValidatingController:
   pass

def fetchPerson() -> Person:
   pass

def retrievePersons() -> list[Person]:
   pass

def getPersonInfo() -> PersonInfo:
   pass



class DtaRcrd10:
    def __init__(self):
        self.genymdhms = "..."
        self.pszquint = "..."
        self.serverProt = "..."


from typing import Protocol
from abc import ABC, abstractmethod

# Option 1: Using Protocol (recommended for interface-like behavior)
class ILabelPrinter(Protocol):
    def print_label(self) -> None:
        ...

class Labeler:
    def __init__(self, label_printer: ILabelPrinter):
        self._str_title: str = "..."
        self._m_first_name: str = "..."
        self._m_str_last_name: str = "..."
        self._i_label_printer: ILabelPrinter = label_printer
    
    def print_address(self):
        # Implementation here
        pass




from typing import List
class Labeler:
  def __init__(self, printer = None):
    self._a: List[str] = []
    self.printer = printer
  
  def print_address_line(self):
    for i in range(len(self._a)):
      self.printer.print_line(self._a[i])




class Labeler:
  def prAL() -> None:
    pass


from typing import Protocol
from abc import ABC, abstractmethod
class ShoppingCart(Protocol):
    def checkout(self) -> None:
        ...

class ShoppingCartLoggingDecorator(ShoppingCart):
  def __init__(self, delegate: ShoppingCart, logger):
    self.__delegate: delegate
    self.__logger: logger

  def checkout(self) -> None:
    self.__logger.log("Checkout started")
    self.checkout()
    self.__logger.log("Checkout done")



class Person:
  def __init__(self):
    self.firstName = ""
    self.lastName = ""
    self.personState = ""
    self.addrStreetAndNo = ""
    self.addrZipAndCity = ""
    self.addrState = ""