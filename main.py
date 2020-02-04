class ROI:
    
    def getIncome(self):
        self.income = input("Enter Total Monthly Income: ")
        return self.income
    
    def getExpenses(self):
        self.expenses = input("Enter Total Monthly Expenses: ")
        return self.expenses
    
    def getCashFlow(self, num1, num2):
        self.cashFlow = int(num1)-int(num2)
        return self.cashFlow
    
    def CashonCashROI(self, num1):
        self.annual = int(num1)*12
        self.investment = input("Enter Total Investment on Property: ")
        self.ROI = int(self.annual)/int(self.investment)
        return self.ROI

myROI = ROI()
myIncome = myROI.getIncome()
myExpenses = myROI.getExpenses()
myCashFlow = myROI.getCashFlow(myIncome, myExpenses)
ReturnOnInvestment = myROI.CashonCashROI(myCashFlow)
print("Your ROI is: {}" .format(ReturnOnInvestment))