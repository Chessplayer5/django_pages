import random

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
play_again = "yes"
while play_again == "yes":
    sum = 0
    turn = "hit"
    while turn == "hit":
        sum += random.choice(card_values)
        print("You currently have: " + str(sum))
        turn = input("What do you want to do? ")

    if sum == 21:
        print("You got Blackjack!")
    elif sum > 21:
        print("You lost")
    else:
        print("You stopped at: " + str(sum))

    play_again = input("Want to play again? ")
