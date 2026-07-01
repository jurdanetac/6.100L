## 6.100L PSet 1: Part A
## Name: Juan Urdaneta
## Time Spent: 00:30
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

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

print(f"Number of months: {months}")
