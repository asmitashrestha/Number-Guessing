actual_number = 55
counts = 0

while True:
    counts+=1
    guess=int(input("Guess the number"))
    if guess<actual_number:
        print("your guess is too low")

    elif guess>actual_number:
        print("your guess is too low")

    else:
        print(f"You guessed the number in {counts} counts")
        break
print("Thank you for playing this game !!")      
