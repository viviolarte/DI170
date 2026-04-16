# Ask the user to enter favorite fruits
fruits_input = input("Enter your favorite fruits separated by spaces: ")

# Convert the string into a list
favorite_fruits = fruits_input.split()

# Ask for another fruit
fruit_choice = input("Enter the name of a fruit: ")

# Check if the fruit is in the list
if fruit_choice in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

