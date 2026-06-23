from temp_converter import converter  # imported converter class from temp_converter module
from guessing_game import guess_game  # imported guess_game class from guessing_game module

while True:
    print("Choose between options:")
    print("1. Temperature Converter")
    print("2. Random number guessing game")
    print("3. exit")
    ch = int(input("Enter the option: "))

    if ch == 1:
        print("1.Convert celsius to farenheit")
        print("2.Convert farenheit to celsius")

        opt = int(input("Enter the option:"))
        if opt<1 or opt>2:
            print("invalid option!")
            break
        c = converter()  # created an obj

        # based on the conversion (C <-> F) getting the inputs and passing as arguments
        if opt == 1:
            TempInput = float(input("Enter the temperatures(°C):"))
            ans = c.calc(opt, TempInput)
        else:
            TempInput = float(input("Enter the temperatures(°F):"))
            ans = c.calc(opt, TempInput)
        print(ans)

    elif ch == 2:
        # obj for guessing game module
        obj = guess_game()
        obj.game()

    else:
        print("exiting..")
        break