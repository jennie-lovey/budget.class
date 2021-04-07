class Budget:
    def __init__(self,name):
        self.name = name
        self.budgetList = []

    def depositFund(self,amount,description):
        self.budgetList.append({
            'description': description,
            'amount': amount
        })
    def withdrawFund(self,amount,description):
        if self.getBudgetBalance() > amount:
            self.budgetList.append({
                'description': description,
                'amount': -amount
            })
            return True
        return False
    def getBudgetBalance(self):
        amount = 0
        for item in self.budgetList:
            amount += item['amount']
        return amount
    def transferFund(self,amount,budgetCategory):
        self.withdrawFund(amount,f"Transfer fund to {budgetCategory.name}")
        if self.getBudgetBalance() > amount:
            budgetCategory.depositFund(amount,f"Transfer funds from {self.name}")
        


 
    def show(self):
        print(f"{self.name} balance *****{self.getBudgetBalance()}")
        for item in self.budgetList:
            print( f" {item ['description']}.....{item['amount']}")
        





food = Budget('food')
entertainment = Budget('entertainment')
clothing = Budget('clothing')

food.depositFund(10000,'Cowbwell Milk')
food.withdrawFund(3000,'Beans')
food.transferFund(1000,clothing)
print(clothing.show())

entertainment.depositFund(10000,'dancing')
entertainment.withdrawFund(5000,'music')
entertainment.transferFund(10000,food)
print(food.show())


clothing.depositFund(5000,'shorts')
clothing.withdrawFund(5000,'wardrobe')
clothing.transferFund(10000,entertainment)
print(entertainment.show())