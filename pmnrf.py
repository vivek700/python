
donation_list = []
total_employees = int(input("Enter the total number of employees: "))

if total_employees < 3:
    print("Employees cannot be less than 3")
    exit()

for i in range(total_employees):
    amount = int(input("Enter amount: "))
    if amount <= 0:
        print("Amount should be greater than 0")
        exit()
    donation_list.append( amount)

donation_list.sort()

least_number  = int(input("Enter the least number for product: "))
if least_number > total_employees:
    print("Employees cannot be less than least number.")
    exit()

donation_amount = 1
for i in range(least_number):
    donation_amount = donation_amount * donation_list[i]

print(donation_amount)


