def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
    return pay

try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    
    salary = computepay(hours, rate)
    
    print("Salary: $%s" %salary)
    
except ValueError:
    print("Error, Please enter proper numeric input.")
