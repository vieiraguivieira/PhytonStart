

parrot = "Norwegian Blue"

print(parrot[0:6:2])  #Nre - 2 by 2
print(parrot[0:6:3])  #Nw - 3 by 3

number = "9,223;372:036 853,775;807"
separators = number[1::4]
print("Separators: " + separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


