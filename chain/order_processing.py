
class Order:
  def __init__(self):
    self.shoppingCart = ShoppingCart()
    self.customer = Customer()
    self.billingAddress = Address()
    self.shippingAddress = Address()
    self.paymentData = PaymentData()
    self.invoice = Invoice()

class ShoppingCart:
  def __init__(self):
    self.items = []

class Customer:
  def __init__(self):
    self.name = ""
    self.banned = False

class Address:
  def __init__(self):
    self.streetAndNumber = []
    self.zipCode = ""
    self.city = ""
    self.country = ""

class PaymentData:
  def __init__(self):
    self.method = ""
    self.cardNumber = ""
    self.expires = ""
    self.ccv = ""

class Invoice:
  def __init__(self):
    self.total = 123

class OrderError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)
    

class OrderProcessor:
  def processOrder(
      self,
      shoppingCart: ShoppingCart, customer: Customer, 
      billingAddress: Address, shippingAddress: Address,
      paymentData: PaymentData
    ) -> Order:
    self.validateCustomerInput(customer, billingAddress, shippingAddress, paymentData)
    
    self.checkCustomerAccount(customer)

    self.validateShoppingCart(shoppingCart)

    self.createInvoice(shoppingCart, customer, billingAddress, shippingAddress,
      paymentData)

    self.startPaymentProcess(shoppingCart, customer, billingAddress, paymentData)
    return Order()
  
  def validateCustomerInput(self, customer: Customer, billingAddress: Address, shippingAddress: Address,
      paymentData: PaymentData):
    if customer.name.__len__() < 1:
      raise OrderError("customer name is missing")
  
  def checkCustomerAccount(self, customer: Customer):
    if customer.banned == True:
      raise OrderError("Customer hs been banned from ordering")
  
  def validateShoppingCart(self, shoppingCart):
    if shoppingCart.items == []:
      raise OrderError("shoppingCart is empty")
  
  def createInvoice(self, shoppingCart: ShoppingCart, customer: Customer, billingAddress: Address, shippingAddress: Address,
      paymentData: PaymentData):
    pass
  
  def startPaymentProcess(self, shoppingCart: ShoppingCart, customer: Customer, billingAddress: Address, paymentData: PaymentData):
    pass
  
