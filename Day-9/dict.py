programing_dictionary = {
    "Bug": "A bug is an error, flaw, or fault in a program", 
    "Function": "A function is a block of reusable code that performs a specific task",
    }

print(programing_dictionary["Bug"])

programing_dictionary["Loop"] = "the action of doing something over again"
print(programing_dictionary)

empty_dictionary = {}

#wipe existing dictionary

#programing_dictionary = {}
#print(programing_dictionary)

#edit an item in dictionary
programing_dictionary["Bug"] = "a moth in computer"
print(programing_dictionary)

# loop through dictionary

for thing in programing_dictionary:
    print(thing)
    print(programing_dictionary[thing])