
# a function is a small reusable chunk of code

# a basic funstion is defined as follows
def my_function(): # the function definition
    pass # the function body is independent 


def say_hello():
    print("hello")

def insult():
    print("poopoo stinky")

# to call a function, use the name and parenthesis
say_hello()
insult()

# functions with paramaters
def greet_person(name, age): # name is a parameter
    print("hello ", name)
    print("you are ", age, " years old")


#call a function, and pass an argument
greet_person("connor", 24)
greet_person("stoopid", 69)


# returning values from functions
def add_two_numbers(number_one, number_two):
    output = number_one + number_two
    return output # gives the value back to whoever called it 

# capture the output from add_two_numbers
function_output = add_two_numbers(2, 2)

print(function_output)
