import random
import time

# defining guessing game as a function
def guessing_game():
    print("------------Starting Guessing Game------------")
    time.sleep(2)
    # defining a range from 1 to 100
    number_range = random.randint(1, 100)
    # Storing computer generated integer as 'n'
    n = number_range
    j = 0
    try:
        while True:
            # asking user to Guess a number
            i = int(input("Please Guess a Number: "))
            # giving an nested if condition to compare i with n
            # if i is greater than n
            if i > n:
                # when subtracting i with n if the result is greater than 20. Raise an error and a Hint.
                if i - n > 20:
                    j += 1
                    print("Incorrect Guess, [Hint: Please Enter a lower number]", n)
                # when subtracting i with n if the result is greater than 10 but less than 20. Raise an Error and a Hint.
                elif 10 < i - n <= 20:
                    j += 1
                    print("Incorrect Guess , [Hint: Please Enter a a bit lower number]")
                # when subtracting i with n if the result is greater than 5 but less than 10. Raise an Error and a Hint
                elif 5 < i - n <= 10:
                    j += 1
                    print("Incorrect Guess, [HInt: (Answer Nearby) Please Guess a bit lower than a bit]")

                else:
                    j+1
                    print("Cannot Generate Hint, Error Reason (Answer too close)")
            elif i < n:
                if n - i > 20:
                    j += 1
                    print("Incorrect Guess, [Hint: Please Enter a Greater Number]")
                elif 10 < n - i <= 20:
                    j += 1
                    print("Incorrect Guess, [HInt: Please Enter a bit greater Number]")
                elif 5 < n - i <= 10:
                    j += 1
                    print("Incorrect Guess, [Hint: (Answer Nearby) Please Enter a bit greater than a bit]")
                else:
                    j+=1
                    print("Cannot Generate Hint, Error Reason: Answer too close")
            elif i == n:
                j += 1
                print("Correct Answer!, Tried", j, 'times')
                break
    except ValueError:
        print("Do not abuse the Program Please Enter Numbers only")
    except TypeError:
        print("Do not abuse the Program Please Enter Numbers only")


guessing_game()
