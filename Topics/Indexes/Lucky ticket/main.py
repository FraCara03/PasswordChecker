# Save the input in this variable
ticket = input()

# Add up the digits for each half
access_1 = ticket[0:3]
access_2 = ticket[-3:]
half1 = 0
half2 = 0

for number in access_1:
    half1 += int(number)

for number in access_2:
    half2 += int(number)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
