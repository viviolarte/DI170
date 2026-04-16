class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Luna", 40)


# Step 3: Print Dog Details and Call Methods
print(f"Dog 1: {davids_dog.name}, Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print()

print(f"Dog 2: {sarahs_dog.name}, Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()


# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}")
else:
    print("Both dogs are the same height")