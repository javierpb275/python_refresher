friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(4):
    print(f"{friend} is my friend.")

grades = [35, 67, 98, 100, 100]
total = 0
total_2 = sum(grades)
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)
print(total_2 / amount)

number = 7

while True:
    user_input = input("would you like to play? (Y/n)")
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong.")