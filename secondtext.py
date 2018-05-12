def pause():
  input()

def mid():
    s1 = ("You are the host of a party, and you have invited many of your highschool friends over")
    print(s1)
    pause()
    s2 = ("After an hour or so, your house is filled to the brim with some of your best friends,")
    print(s2)
    pause()
    s3 = ("Henry")
    print(s3)
    pause()
    s4 = ("Adreany")
    print(s4)
    pause()
    s5 = ("Mishael")
    print(s5)
    pause()
    s6 = ("And so on")
    print(s6)
    pause()
    s7 = ("There was one person that you were particuarly looking for that did enter the front door but disappeared into the night")
    print(s7)
    pause()
    s8 = ("Nowhere to be found, you started looking into the rooms to see if your friend was still a guest in your party")
    room_choice_m = []

    bedroom_m = "bedroom"
    kitchen_m = "kitchen"
    party_room_m = "partyroom"
    dining_room_m = "diningroom"
    backyard_m = "backyard"
    bathroom_m = "bathroom"

    rooms_m = [bedroom, kitchen, party_room, dining_room, backyard, bathroom]
    choose_m = input("Which Room will you like to pick?: ").format[room_choice_m]
    if room_choice_m == "bedroom" == True:
        print("Oh")
