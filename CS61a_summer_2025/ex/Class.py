"""
如果属性名称以下划线开头，则只能在类本身的方法中访问它，而不是用户访问。
使用.来调用实例的方法，.左边的类名就是绑定到方法中的self形参。
"""


class Account:
    """实现一个银行账户
    >>> a = Account('sala')
    >>> a.interest
    0.02
    >>> a.deposit(100)
    100
    >>> a.withdraw(5)
    95
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


class SaveingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)


class AsSeenOnTVAccount(CheckingAccount, SaveingsAccount):
    """
    多重继承， 可以继承多个类的属性和方法
    """

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1


class Bank:
    """一个银行类的实现
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """

    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1
