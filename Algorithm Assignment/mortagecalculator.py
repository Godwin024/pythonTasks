principal = int(input("Enter the principal: "))
annual_interest_rate = float(input("Enter the anual interst rate: "))
time_duration = int(input("Enter the duration of the mortage: "))
monthly_payment = 0


monthly_payment = principal * annual_interest_rate * (1 + annual_interest_rate) ** time_duration // (1 + annual_interest_rate) ** time_duration - 1

print("Your monthly payment is: ", monthly_payment,"$")




