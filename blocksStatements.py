name = input("Please enter your name: ")
age = int(input("How old are you? {0}? ".format(name)))

# if age >= 18:
#     print("You can vote!")
#     print("Please put an X in the box.")
# else:
#     print("You're not old enough to vote. You may vote in {0} years.".format(18 - age))

#debugging
if age < 18:
    print("You're not old enough to vote. You may vote in {0} years.".format(18 - age))
elif age == 900:
    print("You're lying!")
    # elif é else if
else:
    print("You can vote!")
    print("Please put an X in the box.")
