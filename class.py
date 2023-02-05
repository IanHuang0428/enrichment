# class Account:
#     def __init__(self, number, name):
#         self.number = number
#         self.name = name
#         self.balance = 0
        
#     def deposit(self, amount):  #存款動作: amount代表存入金額
#         if amount <= 0:
#              print("Error!")
#         self.balance += amount
        
#     def withdraw(self, amount): #取款動作: amount代表取款金額
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Error!")

# #建立account 1
# account1 = Account("S00001", "AAA")
# account1.deposit(1000)              #存入1000
# print(account1.balance)

# #建立account 2
# account2 = Account("S00002", "BBB")
# account2.deposit(2000)              #存入2000
# print(account2.balance)






# #Python允許在物件生成階段，再進行屬性的定義
# class Account:
#     pass

# def deposit(acct, amount):
#     if amount <= 0:
#         raise ValueError('must be positive')
#     acct.balance += amount
       
# def withdraw(acct, amount):
#     if amount <= acct.balance:
#         acct.balance -= amount
#     else:
#         raise RuntimeError('balance not enough')
        
# acct = Account()
# acct.number = '123-456-789'
# acct.name = 'Justin'
# acct.balance = 0

# print(acct.number)    # 123-456-789
# print(acct.name)      # Justin

# deposit(acct, 100)
# print(acct.balance)   # 100
# withdraw(acct, 50)
# print(acct.balance)   # 50




# 交通工具(基底類別)
class Transportation:
    # 駕駛方法
    def drive(self):
        print("Base class drive method is called.")
# 汽車子類別
class Car(Transportation):
    # 駕駛方法
    def drive(self):
        super().drive()
        print("Sub class drive method is called.")
        
car1 = Car()
car1.drive()