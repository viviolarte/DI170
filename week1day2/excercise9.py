otal_cost = 0
ages = []

num_people = int(input("How many people are buying tickets? "))

for i in range(num_people):
    age = int(input(f"Enter age of person {i+1}: "))
    ages.append(age)

    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print("Ages entered:", ages)
print("Total ticket cost: $", total_cost)