#import we need from the user
#total rent
#total food ordered for snacking
#electricity units spend
#charge per unit
#person leaving in room

##output
#total amount u have to pay is

rent = int(input("enter your flat rent = "))
food = int(input("enter the amount of food orderede = "))
electricity_spend = int(input("enter the total of electricity spend = "))
charge_per_unit = int(input("enter the charge per unit = "))
person = int(input("enter the number of persons living in the flat = "))

total_bill = electricity_spend*charge_per_unit

output =(food+rent+total_bill) // person
print("each person will pay = ",output)
 
