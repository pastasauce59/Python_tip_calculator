print("Welcome to the tip calculator!")

bill = input("what was your total bill? $")
tip = input("How much tip (%) would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_as_float = float(bill)
tip_as_percent = int(tip)/100 + 1
people_as_int = int(people)

final_amount = "{:.2f}".format( (bill_as_float * tip_as_percent) / people_as_int )

message = f"Each person should pay: ${final_amount}"

print(message)
