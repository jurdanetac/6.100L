## 6.100L PSet 1: Part C
## Name: Juan Urdaneta
## Time Spent: 03:00
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_house = 800_000
down_payment = cost_of_house * 0.25
months_in_three_years = 36
r = None
steps = 0
epsilon = 100


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if initial_deposit >= down_payment:
    r = 0.0
else:
    # 0%----------r-----------100% of initial deposit
    low = 0.0
    high = 1.0
    r = high
    amount_saved = initial_deposit * (1 + r / 12) ** months_in_three_years

    if amount_saved < down_payment:
        r = None
    else:
        while abs(amount_saved - down_payment) > epsilon:
            steps += 1

            if amount_saved < down_payment:
                low = r
            elif amount_saved > down_payment:
                high = r

            r = (low + high) / 2
            amount_saved = initial_deposit * (1 + r / 12) ** months_in_three_years

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")
