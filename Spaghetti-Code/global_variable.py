current_number = 0

def increment_number():
    global current_number
    current_number += 1

def reset_number():
    global current_number
    current_number = 0

def print_number():
    global current_number
    print(current_number)

def check_number():
    global current_number
    if current_number > 10:
        print("Number is greater than 10")
    elif current_number < 5:
        print("Number is less than 5")
    else:
        print("Number is between 5 and 10")

increment_number()
increment_number()
reset_number()
print_number()
increment_number()
check_number()