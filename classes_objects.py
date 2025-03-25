# class Car:
    # pass

# my_car = Car()

# print(type(my_car))





# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model =  model
#
#     def display_info(self):
#         print(f"Car: {self.brand} {self.model}")
#
# car1 = Car("Toyota", "Corolla")
# car1.display_info()



#
# class Person:
#  def __init__(self, name, age):
#   self.name = name
#   self.age = age
#
#  def introduce(self):
#   print(f"My name is {self.name} and I am {self.age} years old")
#
# person1 = Person("Alice", 32)
# person1.introduce()




# class Employee:
#     company = "TechCorp"
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# emp1 = Employee("Ram", 50000)
# emp2 = Employee("Ron", 60000)
#
#
# print(emp1.name, emp1.company, emp1.salary)
# print(emp2.name, emp2.company, emp2.salary)





# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(1000)
# account.deposit(500)
#
# print(account.get_balance())