def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")

hint_username("Johnnono")

def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(10))

def fizz_buzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz(15)