import random as r
import time as t


class Account:

    # Q2 계좌 객체 개수
    accountCount = 0

    # Q8 계좌의 객체를 저장합니다.
    accountList = []

    # Q1. Account 생성자
    def __init__(self, owner, initalMoney):
        # 은행이름
        self.bankName = "SC"

        # 계좌번호 생성
        part1 = "".join(r.choices("0123456789", k=3))
        part2 = "".join(r.choices("0123456789", k=2))
        part3 = "".join(r.choices("0123456789", k=6))
        self.accountNumber = f"{part1}-{part2}-{part3}"

        # 잔액
        self.money = initalMoney

        # 예금주
        self.owner = owner

        # Q7 입금횟수
        self.depositCount = 0

        # Q2. 계좌수증가
        Account.accountCount = Account.accountCount + 1

        # Q8. 계좌 객체 추가
        Account.accountList.append(self)

        # Q10. 입/출금 기록
        self.dHistory = []
        self.wHistory = []

    # Q3
    def getAccountNum():
        return Account.accountCount

    def getDeposit(self):
        return self.money

    # Q4
    def deposit(self, inputMoney, depositor):
        if inputMoney >= 1:
            self.money = self.money + inputMoney
            self.depositCount = self.depositCount + 1
            self.interest()

            historyTime = t.strftime("%Y-%m-%d %X", t.localtime(t.time()))
            history = [historyTime, inputMoney, depositor]

            self.dHistory.append(history)
            return True
        else:
            return False

    # Q5
    def withdraw(self, inputMoney, depositor):
        if self.money > inputMoney:  # 잔고가 남아있을때만.
            self.money = self.money - inputMoney

            historyTime = t.strftime("%Y-%m-%d %X", t.localtime(t.time()))
            history = [historyTime, inputMoney, depositor]

            self.wHistory.append(history)
            return True
        else:
            return False

    # Q6
    def displayInfo(self):
        info = [self.bankName, self.owner, self.accountNumber, self.money]
        print(
            f"은행이름: {self.bankName}, 예금주: {self.owner}, 계좌번호: {self.accountNumber}, 잔고: {self.money:,}"
        )
        return info

    # Q7
    def interest(self):
        if self.depositCount >= 5:
            self.depositCount = 0
            self.money = self.money + self.money * 0.01

    # Q10
    def depositHistory(self):
        for i in range(len(self.dHistory)):
            print(
                f"{self.dHistory[i][0]}, {self.dHistory[i][1]}, {self.dHistory[i][2]}"
            )

    def withdrawHistory(self):
        for i in range(len(self.wHistory)):
            print(
                f"{self.wHistory[i][0]}, {self.wHistory[i][1]}, {self.wHistory[i][2]}"
            )

    def isRich(self, money):
        if money >= 1000000:
            return True
        else:
            return False

    def foundRich(self):
        for customer in Account.accountList:
            if self.isRich(customer.getDeposit()):
                customer.displayInfo()


def main():
    overSeer = Account("관리자", 0)

    customer1 = Account("김진서", 10000)
    customer2 = Account("이원준", 1000000)
    customer3 = Account("백채은", 20000)

    customer1.displayInfo()
    customer2.displayInfo()
    customer3.displayInfo()

    print(overSeer.accountList)  # 관리자 포함 4개 Q8 리스트에 저장된것을 호출

    for i in range(5):
        customer1.deposit(10, "아이펠")  # 돈 입금자명포함하여 입금
    customer1.displayInfo()  # 5번 입금했으니 이자 지급

    for i in range(5):
        customer1.withdraw(10, "괴도키드")  # 돈 출금자명포함하여 출금
    customer1.displayInfo()

    overSeer.foundRich()  # 백만원 이상인 사람만 호출합니다.

    customer1.depositHistory()  # 1번고객의 입금내역을 출력합니다
    customer1.withdrawHistory()  # 2번 고객의 읍금내역을 출력합니다.


main()
