# import helper as h
# print("Importing 'helper' from 'main'.")
# from helper import extract_lower, extract_upper

# print("Importing 'extras' from 'main'.")
import helper
import extras

# print(f"__name__ in main.py: {__name__}")

# name = 'Anshul Jain'
print(f"Lowercase Letters: {helper.extract_lower(extras.name)}")
print(f"Uppercase Letters: {helper.extract_upper(extras.name)}")