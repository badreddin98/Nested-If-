#Task 1: Code Correction:
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else :
      action = "cross a river"
      print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    action2 = input("do you want to light a torch or proceed in the dark? ")
    if action2 == "light a torch":
        print("You find a hidden treasure!")
    elif action2 == "proceed in the dark":
        print("be careful you might fall")
    else:
        pass
else:
    pass




