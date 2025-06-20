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


def init():
    # get the port from env or use default
let portAsString = process.env.port;
let defaultPort = 8080;
let port = portAsString == null ? defaultPort : +portAsString;

// start server on given port
console.log(port);
}