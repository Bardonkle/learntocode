my_list = [1, 2, 3, 4]

# first_element equals the first (zeroth) position in my_list
first_element = my_list[0]

# new_list = range(10)

my_list.append(5)

print(my_list)

# tuples are immutable (cannot be changed)
my_tuple = (1, 2, 3, 4, 5)

my_tuple_value = my_tuple[2]

print(my_tuple_value)


my_iterable = [1, 2, 3, 4]

for number in my_iterable:
    new_number = number + 1
    print(new_number)
print("done")

x = 15
while True:
    x = x - 1

    # if x modulo 2 is equal to 0 
    # modulo -> remainder of division
    if x % 2 == 0:
        print(x)

    if x == 1:
        break

print("done")

credentials = ["connor", "Password1!"], ["Bingus, FooBar1"]

