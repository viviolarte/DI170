# Step 0: Provided Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Step 1: Create three cat objects
cat1 = Cat("Milo", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Simba", 5)


# Step 2: Create a function to find the oldest cat
def find_oldest_cat(c1, c2, c3):
    oldest = c1

    if c2.age > oldest.age:
        oldest = c2
    if c3.age > oldest.age:
        oldest = c3

    return oldest


# Step 3: Print the oldest cat’s details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")