# Day 8 - OOP Classes and Objects
# Author: Vishvi
# Date: 2026-07-24

# CONCEPT 1 - Basic Class
class Student:
    def __init__(self, name, age, marks):
        self.name  = name
        self.age   = age
        self.marks = marks

    def introduce(self):
        print(f'Hi! I am {self.name}, {self.age} years old')

    def get_grade(self):
        if self.marks >= 90:   return 'A'
        elif self.marks >= 75: return 'B'
        elif self.marks >= 60: return 'C'
        elif self.marks >= 40: return 'D'
        else:                  return 'F'

    def result(self):
        print(f"{self.name}: {self.marks} | Grade: {self.get_grade()} | {'PASS' if self.marks >= 40 else 'FAIL'}")

s1 = Student('Vishvi', 23, 92)
s2 = Student('Aditi',  25, 75)
s3 = Student('Rohan',  22, 35)
s1.introduce()
s1.result()
s2.result()
s3.result()

# CONCEPT 2 - Inheritance
class DataScientist(Student):
    def __init__(self, name, age, marks, skills):
        super().__init__(name, age, marks)
        self.skills = skills

    def introduce(self):
        super().introduce()
        print(f'Skills: {chr(44).join(self.skills)}')

ds = DataScientist('Vishvi', 23, 92, ['Python', 'SQL', 'ML'])
ds.introduce()
ds.result()

# CONCEPT 3 - BankAccount Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. Balance: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds!')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. Balance: {self.balance}')

    def __str__(self):
        return f'Account({self.owner}, Balance: {self.balance})'

acc = BankAccount('Vishvi', 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)
print(acc)
