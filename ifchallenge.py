name = input("What's your name? ")
age = int(input("How old are you? "))

if 18 < age <= 29:
    print("Welcome to the holidays {}!".format(name))
else:
    print("Go away {}!! You are {} years old!".format(name, age))

# tim solution
# name = input("Please enter your name: ")
# age = int(input("How old are you? "))

# if 18 <= age < 31:
#    print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#    print("I'm sorry, our holidays are only for cool people")
