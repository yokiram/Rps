#rock paper scisor game
import random
while True:
    choices = ["rock",'paper','scisor']

    print("choices list {}".format(choices))

    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("choose yours ").lower()

#print(computer)


#draw statement
    if player == computer:
        print("computer",computer)
        print("player",player)
        print("draw")

#computer choose rock
    elif computer == "rock":
        if player == "scisor":
            print("computer",computer)
            print("player",player)
            print("player lose")
        if player == "paper":
            print("computer",computer)
            print("player",player)
            print("player win")

#computer choose scisor

    elif computer == "scisor":
        if player == "paper":
            print("computer",computer)
            print("player",player)
            print("player lose")
        if player == "rock":
            print("computer",computer)
            print("player",player)
            print("player win")

#computer choose paper

    elif computer == "paper":
        if player == "scisor":
            print("computer",computer)
            print("player",player)
            print("player lose")
        if player == "rock":
            print("computer",computer)
            print("player",player)
            print("player win")

