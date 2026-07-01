## 6.100L PSet 1: Part B
## Name: Juan Urdaneta
## Time Spent: 00:15
## Collaborators: None

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
monthly_rate_of_return = r / 12
amount_down_payment = cost_of_dream_home * portion_down_payment
amount_saved_monthly = (yearly_salary / 12) * portion_saved

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months = 0
while amount_saved < amount_down_payment:
    amount_saved += amount_saved * monthly_rate_of_return
    amount_saved += amount_saved_monthly
    months += 1

    if months % 6 == 0:
        semi_annual_salary = yearly_salary / 2
        yearly_salary = (semi_annual_salary + (semi_annual_salary * semi_annual_raise)) * 2
        amount_saved_monthly = (yearly_salary / 12) * portion_saved

print(f"Number of months: {months}")

