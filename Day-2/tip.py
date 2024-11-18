bill = float(input("what was the total bill? $"))
tip = int(input("what percent are you giving? 10, 12 or 15? "))
people = int(input("how many people are paying? "))

tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final = round(bill_per_person, 2)
print("each person should pay: $" + str(final))

