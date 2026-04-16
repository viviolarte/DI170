users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

char_to_index = {}

for i in range(len(users)):
    char_to_index[users[i]] = i
    print(char_to_index)
    {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
    index_to_char = {}

for i in range(len(users)):
    index_to_char[i] = users[i]

print(index_to_char)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# 1
char_to_index = {name: i for i, name in enumerate(users)}

# 2
index_to_char = {i: name for i, name in enumerate(users)}

# 3
sorted_dict = {name: i for i, name in enumerate(sorted(users))}

print(char_to_index)
print(index_to_char)
print(sorted_dict)

