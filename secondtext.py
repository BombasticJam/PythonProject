import thirdtext as tt


def search(iterable, obj):
  """ Returns list of indices where obj can be found in iterable """
  return [index for index, item in enumerate(iterable) if item == obj]

def is_subset(subset, superset):
  """ Returns True if every item in subset is also in superset """
  return all([i in superset for i in subset])

def pause():
  input()


def pick_1():
    room_choice_m = []
    rooms_m = {"bedroom": "Looks like there is nothing but sadness here. It seems very empty since there are many couples that came to my party. It wouldn't be empty if she were to appear but she hasn't yet.",
                "kitchen": "As you enter the room, you see a very startling sight. Your friend is there on the floor, gasping for air as she tries to tell you something.",
                "party_room": "The deep booming sound of dance music soars throughout the air and rhythms with the people around the room. It seems as if they are enjoying it *Even though you haven't really put any effort in making this party*. Yet, there was still no sight of her.",
                "dining_room": "Nothing but the sounds of crunching chips and the smell of leftover beer that was spilled on the floor. But there was still no sight of her.",
                "backyard": "As you exit into your backyard, you smell a whiff of smoke, which smells like a normal cigar. ",
                "bathroom": "bathroom",
                }
    rooms_m1 = ['bedroom', 'kitchen', 'party_room', 'dining_room', 'backyard', 'bathroom']
    print(rooms_m1)

    choose_m1 = input("Which Room will you like to pick?: ").format(room_choice_m)

# choose_m2 = input("Please choose another room:  ").append(format(room_choice_m))

    if choose_m1 in rooms_m1:
        print(rooms_m[choose_m1])
        if not "bathroom":
            choose_m1 = input("Please choose another room:  ").append(format(room_choice_m))
    else:
        print("Please try to search in an existing room")
    pick_1()

def mid():
    s1 = ("You are the host of a party, and you have invited many of your highschool friends over")
    print(s1)
    pause()
    s2 = ("After an hour or so, your house is filled to the brim with some of your best friends,")
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

