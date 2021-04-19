
# dictionary is a way to store key-value pairs
# a record in a dictionary looks like "key": "value"
# where key is the key to the record, and value can be any type

from pprint import pprint

my_dict = {
    "juice": "a tasty drink",
    "apple": "a fruit thats grows on trees"
}

my_value = my_dict["juice"]

print(my_value)


# upsert (update or insert)
my_dict["apple"] = "a round, red fruit that grows on trees"
my_dict["coke"] = "favorite thing to snort"

pprint(my_dict)

# PROGRAM: Create a program to find the most used letter in a sentence
# ALGORITHM TO ACCOMPLISH PROGRAM
# 1. get input
# 2. for every letter in the sentence
# 3. check to see if it is a space or a symbol
# 4. IF the letter is a symbol, go to the next letter
# 5. lowercase the letter, because we dont want the capital letters
# 6. if the letter is not in the dictionary, add a record with a value of 1
# 7. otherwise, add 1 to the value of the letter
# 8. repeat until end of string

sentence = "the quick brown fox jumps over the lazy dog. then it fell on its face"

# create a dictionary to store letters by their occurance in the sentence
letters_dict = {}

# loop over every letter in the sentence, and update the dictionary
for letter in sentence:
    # if the letter is a space or symbol, skip it 
    if letter in ". !@#$%^&*(){}":
        continue

# lowercase the current letter
    letter = letter.lower()

    if not letters_dict.get(letter):
        # if the letter is not in the dictionary, create it and give it the value 1
        letters_dict[letter] = 1
    

    else:
        # if the letter IS in our dictionary, add one to the value 
        # same as -> letter_dict[letter] = letter_dict[letter] + 1
        letters_dict[letter] += 1

# find the max value of letters_dict
max_value = max(letters_dict, key=letters_dict.get)
print (max_value)




