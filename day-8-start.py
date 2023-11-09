#Simple function
# def greet():
#     print("hello")
#     print("hallo")
#     print("guten morgen")
    

# greet()

#function that allows for input
# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"hallo {name}")
#     print(f"guten morgen {name}")

# greet_with_name("Liz")

# Functions with more than 1 input
# positional arguments
# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Liz", "Virginia")

# Key word arguments
def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}")

greet_with(location = "Virginia", name = "Liz")