def pause():
  input()


def pick_1():
    room_choice_m = []
    rooms_m = {"bedroom": "Looks like there is nothing but sadness here. It seems very empty since there are many couples that came to my party. It wouldn't be empty if she were to appear but she hasn't yet.",
                "kitchen": "As you enter the room, you see a very startling sight. Your friend is there on the floor, calling for help with the last calls she can manage to speak.",
                "partyroom": "The deep booming sound of dance music soars throughout the air and rhythms with the people around the room. It seems as if they are enjoying it *Even though you haven't really put any effort in making this party*. Yet, there was still no sight of her.",
                "diningroom": "Nothing but the sounds of crunching chips and the smell of leftover beer that was spilled on the floor. But there was still no sight of her.",
                "backyard": "As you exit into your backyard, you see a raccoon running into your trashcans. You do nothing but stare at it as it feasts on the overloaded trashcan. Suddenly, you go back into motion and try to knock down the raccoon with the trashcan itself and you succeeded. However, you soon remembered that you were trying to find someone, so you go back to searching. ",
                "bathroom": "As you go open the bathroom door, you notice that it's locked. You hear a voice inside, telling you to go away and to give her privacy, which you did but still, nothing to see here. ",
                }

    print("\nbedroom", "\nkitchen", "\npartyroom", "\ndiningroom", "\nbackyard", "\nbathroom")

    choose_m1 = input("Which Room will you like to pick?: ").format(room_choice_m)


    if choose_m1 in rooms_m:
        print("\n\n\n\n\n\n",rooms_m[choose_m1])
        if choose_m1 != "kitchen":
            print("\n")
            return pick_1()
        if choose_m1 == "kitchen":
            input()
            print("\n\n\n\n\n\n")
    else:
        print("Please try to search in an existing room")
        pick_1()


def mid():
    s1 = ("You are the host of a party, and you have invited many of your old highschool friends over")
    print(s1)
    pause()
    s2 = ("After an hour or so, your house is filled to the brim with some of your friends,")
    print(s2)
    pause()
    s3 = ("Henry,")
    print(s3)
    pause()
    s4 = ("Adreany,")
    print(s4)
    pause()
    s5 = ("Mishael,")
    print(s5)
    pause()
    s6 = ("And so on.")
    print(s6)
    pause()
    s7 = ("There was one person that you were particuarly looking for that did enter the front door but disappeared into the night")
    print(s7)
    pause()
    s8 = ("Nowhere to be found, you started looking into the rooms to see if your friend was still a guest in your party")
    print(s8)
    pause()
    pick_1()
