import random 
class guess_game:
    def game(self):
        randomNumber = random.randint(1, 100)
        flag = False
        print("A random number guessing game(Range:1-100)")
        print("Three chances")
        n = 3
        for i in range(n):
            print(f"chance no:{i+1}")
            userInput = int(input("Enter the number you guess(1-100):"))
            if userInput < 1 or userInput > 100:
                print("Number out of bounds!")
                continue
            if userInput == randomNumber:
                print("You guessed the correct number!")
                print("Game Over!")
                return
            if userInput < randomNumber:
                print("Too low!")
            else:
                print("Too high!")

            print(2 - i, "chances left")

        if not flag:
            print("The random Number gernerated is ",randomNumber)
        else:
            print("Game Over!")