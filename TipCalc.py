#Ask the user for the total bill amount & level of service (good, bad, or fair)
#Then calculate the tip amount and the total amount
#Then calculate the tip good >= 20%, fair >= 15%, bad >= 10%


total_bill = int(input("Total Bill Amount?"))

level_of_service = input("Was your level of service good, bad, or fair?")

good = 1.2
fair = 1.15

if level_of_service == "good":
    print("Your final bill is: ","$", (total_bill * good ))
elif level_of_service == "fair":
        print("Your final bill is: ","$", (total_bill * fair))
else: 
    # print ("Your final bill is: ","$", (total_bill * 1.1))
    print ("Your final bill is: $%.2f %s" % (total_bill * 1.1, "yes"), "have a good day")
    # print(f"Your final bill is: ${total_bill * 1.1}")





#Setup
# The amounts for tips based on the level of service
# - Good = 20%
# - Fair = 15%
# - Bad = 10%
service_good = 0.2
service_fair = 0.15
service_bad = 0.1
service_whatever = .05

# Do the work
#  Prompt the user for
total_bill = float(input("Total bill amount? "))
# Total bill
print(total_bill)
level_of_service = input("Level of service? ")
# Level of service
print(level_of_service)


#3. Return the result
# Example session:
# tip amount: $20.00
# Total bill amount? 100
# Level of service? good 
#

split_by = int(input("Split by how many ways?"))

if level_of_service == 'good':
    # tip_amount = total_bill * service_good
    service_amount = service_good
elif level_of_service == 'fair':
    # tip_amount = total_bill * service_fair
    service_amount = service_fair
elif:
    # tip_amount = total_bill * service_bad
    service_amount = service_bad
else:
    service_amount = service_whatever

    tip_amount = total_bill * service_whatever

print(f"Tip amount: {tip_amount}") 
# print(f"Total amount: {total_bill + tip_amount}")
print (f"total amount: {total_amount}")

rounded_amount_per_person = round(total_amount / split_by, 2)

print(f"Amount per person: {rounded_amount_per_person}")



