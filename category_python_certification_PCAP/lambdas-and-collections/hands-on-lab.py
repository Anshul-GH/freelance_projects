# 1. Sort the 'people' list of dictionaries alphabetically based on the
# 'name' key from each dictionary using the 'sorted' function and store 
# the new list as 'sorted_by_name'

people = [
    {'name': 'Kevin Bacon', 'age': 61},
    {'name': 'Fred Ward', 'age': 77},
    {'name': 'finn Carter', 'age': 59},
    {'name': 'Ariana Richards', 'age': 40},
    {'name': 'Vicotor Wong', 'age': 74},
]

# sorted_by_name = None # AssertionError
sorted_by_name = sorted(people, key=lambda d: d['name'].lower())

assert sorted_by_name == [
    {'name': 'Ariana Richards', 'age': 40},
    {'name': 'finn Carter', 'age': 59},
    {'name': 'Fred Ward', 'age': 77},
    {'name': 'Kevin Bacon', 'age': 61},
    {'name': 'Vicotor Wong', 'age': 74},
]


# =============================================================================== #

# 2. Use the 'map' function to iterate over 'sorted_by_name' to generate a
# new list called 'name_declarations' where each value is a string with
# '<NAME> is <AGE> years old.' where the '<NAME>' and '<AGE>' values are from
# the dictionary.

# name_declarations = None
# name_declarations = list(map(lambda d: f"{d['name']} is {d['age']} years old", sorted_by_name))
name_declarations = list(
    map(lambda d: f"{d['name']} is {d['age']} years old", sorted_by_name)
)
# print(name_declarations)


assert name_declarations == [
    "Ariana Richards is 40 years old",
    "finn Carter is 59 years old",
    "Fred Ward is 77 years old",
    "Kevin Bacon is 61 years old",
    "Victor Wong is 74 years old",
]