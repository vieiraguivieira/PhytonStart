name = input("Please enter your name: ")
age = int(input("How old are you? {0}? ".format(name)))

if age >= 18:
    print("You can vote!")
    print("Please put an X in the box.")
else:
    print("You're not old enough to vote. You may vote in {0} years.".format(18 - age))
