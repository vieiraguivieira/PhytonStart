letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]  # without "a"
print(backwards)

backwards = letters[25::-1]  # with "a"
print(backwards)

backwards = letters[::-1]  # with "a"
print(backwards)

backwards = letters[16:13:-1]  #qpo
print(backwards)

backwards = letters[4::-1]  #edcba
print(backwards)

backwards = letters[-1:-9:-1]  #last 8
print(backwards)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])