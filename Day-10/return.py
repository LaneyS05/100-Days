def format_name(first, last):
    if first == "" or last == "":
        return "you did not provide valid inputs"

    formated_first = first.title()
    formated_last = last.title()
    return f"{formated_first} {formated_last}"


format_str = format_name(input("what is your first name "), input("what is your last name "))
print(format_str)



def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output_1 = function_2(function_1("hello"))
print(output_1)
