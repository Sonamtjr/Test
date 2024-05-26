import random
secret_number=random.randint(1,10)
max_attempts=3
def welcome_message():
    print("\nWelcome to the Number Guessing game!")
    print(f"You have{max_attempts}attempts to guess the correct number.")
def guess_recursive(attempts_left):
    guess=int(input("\nGuess the number(between 1 to 10): "))
    if guess==secret_number:
        print("Congratulation!you guess the correct number!")
    else:
        print(f"Wrong guess.Attempts left: {attempts_left-1}")
        if attempts_left > 1 :
            guess_recursive(attempts_left - 1)
        else:
            print(f"\nsorry, you couldnt guess the number.The correct number was {secret_number}. ")
welcome_message()
guess_recursive(max_attempts)
print(f"Memory address of secret Number{secret_number} is:{id(secret_number)}")

