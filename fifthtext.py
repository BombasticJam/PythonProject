def pick2():
    rooms = {
            "bedroom" : ["Liliana","Briana", "Kevin", "Howard"],
            "kitchen" :["Nicole","Henry","Arnold","Adrian","Crystal"],
            "partyroom" : ["Pamela","Laisha","Arleen","Andrew","Mishael","John","Daniel","Lanaya"],
            "diningroom" : ["Michael","Edu","Johnathan","Matthew","Amanda"],
            "backyard" : ["June","July","Julissa","Puppy"],
            "bathroom" : ["Jade"]
    }

    people_items = {
        "liliana" : {"wallet":"As you look into her wallet, something fell out of it which made you muffle 'Deja vu' as you picked it up and looked at it. It was a white piece of plastic which looked like a gum wrapper. You put the gum wrapper into your pocket and search the wallet thorough but found nothing but credit cards",
                     "dice": "Just some plain old white dice, nothing to be interested in",
                     "reciept":"Bought 4 bags of fruit (Who needs 4 bags of fruit...) and a limited edition monopoly gameboard",
                     "monopolymoney":"1000 monopoly credits"},
        "briana" : {"purse" :"As soon as Briana handed her purse to you, you looked in it and found absolutley nothing unusual present so you give it back to her",
                    "receipt":"Bought 1 bag of chips (Probably for the party), two liters of soda (Also for the party), and new headphones",
                    "phone":"She doesn't seem to want you to look into her phone so you put it back into her possesion",
                    "headphones":"White and gold headphones by Drake","monopolymoney":"1600 monolpoly credits"},
        "kevin" : {"watch": "A black watch with a stain on the side. The stain is white which seemed like something weird but this is kevin we're investigating so no reason to put him as a suspect",
                   "pencil":"An unsharpened pencil used for keeping track of credits in monopoly",
                   "notebook":"Black and white spotted notebook for writing things on (Duh)",
                   "headphones":"Hot pink headphones that match Kevin's clothing",
                   "monopolymoney":"500 monopoly credits"},
        "howard" : {"wallet":"Only 5 different items including a chapstick, USD Money, photos of his beloved dog, Stacy, four different kinds of credit cards, and a pair of dice",
                    "receipt":"Bought chapstick and a waterbottle",
                    "paper":"White paper from the best company in the world...Dunder Mifflin",
                    "monopolymoney":"2000 monopoly credits"},
        "nicole" : {"toothpick":"A new toothpick ready to be used",
                    "emptywaterbottle":"Plain old plastic taken from the diningroom's supply of beverages ",
                    "purse":"Cosmetics and several strawberry hard candy that you don't the name of",
                    "bracelet":"Silver bracelet made fit for her small wrist"},
        "henry" : {"keychain":"Since Henry thinks you did something to his best friend, he doesn't trust you to look at his keychain",
                   "redcup":"The redcup still had some beer in it but it was very dense looking. He probably snuck some other kind of beer in even though he shouldn't of. The red cup came from the diningroom",
                   "wallet":"Since Henry thinks you did something to his best friend, he doesn't trust you to look into his wallet",
                   "mintgum":"You really hesitated to ask Henry for a piece but you declined yourself before you got picky",
                   "cigarettes":"Cigarettes that really shouldn't be smoked at your house because it could cause the firealarm to go off. That would really worry the guests but distract them"},
        "arnold" : {"bandana":"Black and Blue bandana that he brought to school once, doesn't really seem like his type of style anymore",
                    "wallet":"Nothing but a few reciepts from Walmart",
                    "watch":"Black and gold watch that reminds you of the last prom you had with Crystal. Seems a little too late to talk about it since Crystal can't umm... Just move on to the next item",
                    "matches":"A fire hazard since it can be lit up. Seems like something Henry could use to light up a cig and relax",
                    "phone":"Arnold lends you the phone and you search the recent messages that he has sent to Crystal. The last text message was last month. It seems that Arnold doesn't talk to Crystal as much as Pamela does."},
        "adrian" : {"dogtag":"Max The Doggo",
                    "purse":"Seems weird that he'll be holding a purse but you are reminded that he was with Pamela beforehand of entering the Kitchen. You search anyways and find chapstick, cosmetics, and a couple of candybits",
                    "wallet":"There was nothing but multiple photos of Max, Adrian's dog, and his little sister",
                    "nametag":"White nametag with nothing written on it but the word 'Hello!'",
                    "paper":"Just some good ol' Dunder Mifflin paper",
                    "phone":"You checked for any recent messages with Crystal but found nothing. He barely talks to her but does have a lot of photos of his Dog"},
        "crystal" : {"bloodypieceofpaper":"Seems more of a napkin. You don't touch it because it has been in the Crystal's mouth and seems too bloody to touch",
                     "crystalnecklace":"The very crystalized necklace looks beautiful on her. You were the one who gave her that necklace on her birthday. And it seems like she did enjoy it, since she does love quartz",
                     "bracelet":"A blue gem wearable",
                     "body":"As you try to observe Crystal's body, you don't find that much but you do find that her jacket has been ripped and that she is bleeding from her mouth. Her phone seems to be missing so you really get concerned now. But she still looks beautiful when she sleeps"},
        "pamela" : {"necklace":"Seems weird to have a similar crystal necklace that Crystal recieved for her birthday. However, she is her best friend so it seems reasonable she would adore her things",
                    "bracelet":"Seems weird to have a similar blue gem bracelet that Crystal is wearing. However, it seems that she adores Crystal's fashion",
                    "pen":"A ballpoint pen used for writing good statements",
                    "watch":"A blue watch that matches her blue bracelet",
                    "phone":"She likes to keep her private conversations with Crystal so she didn't want to reveal her phone so you ask her nicely and she just pets you and tells you to stop being nosy"},
        "laisha" : {"deckofcards":"Blue deck of cards that seem worn out",
                    "lipstick":"Red lipstick used for the best of the best",
                    "purse":"Nothing but cosmetics for her looks",
                    "lolipop":"Just a blue cotton candy flavoured lolipop",
                    "headphones":"Pink headphones that seem too big for her",
                    "phone":"A recent message with Crystal was an hour ago. She was asking her where she was at and she said arriving at the party. Laisha's last message was asking her why she was in the Kitchen for so long. That was 10 minutes ago."},
        "arleen" : {"waterbottle":"A waterbottle for the thirst",
                    "smallbackpack":"A red backpack only found in selected stores. That was what the tag said on it",
                    "cosmetics":"Seems related to Laisha's cosmetics. Arleen probably borrowed it for the party",
                    "bubblegum":"You looked at it but put it back before you grabbed a piece for yourself",
                    "phone":"A recent message with Crystal was thirty minutes ago. Arleen asked if she could grab her a few drinks for herself and Arleen. Crystal replied yes and didn't reply back after that"},
        "andrew" : {"headband":"Black addidas headband that isnt sweaty for once",
                    "beer":"Andrew was the only person to actually drink the beer from the bottles from this party. Seemed odd since he used to not like beer",
                    "phone":"No recent messages with Crystal but there were messages that he had left me that you mistakenly didn't look at",
                    "keys":"Seems like normal housekeys",
                    "glasses":"Eyeglasses that Andrew rarley uses"},
        "mishael" : {"bookmark":"A shark bookmark",
                     "seedpackets":"You don't have a clue why Mishael would bring seedpackets to an occasion like this but he did",
                     "card":"An ace of heart",
                     "phone":"No recent text messages from Crystal",
                     "marbles":"Blue and green marbles"},
        "john" : {"cdplayer":"A black cdplayer that is used for playing music",
                  "cddisk":"Cd, probably music",
                  "headphones":"Blue headphones that is probably meant to be used with the cdplayer",
                  "wallet":"Some credit cards and a few bucks but nothing too interesting",
                  "candybar":"Snickers bar; Statisfies the hungry",
                  "redcup":"Looks like John has been to the diningroom before going into the partyroom"},
        "daniel" : {"case":"A case filled with business papers. Daniel has been involved with financial business so he was doing well in his career choice",
                    "businesscard":"Daniel's businesscard",
                    "receipt":"Bought 2 different kinds of paperclips"},
        "lanaya" : {"kitten":"Meow",
                    "hamster":"Lanaya does love her animals so she does bring them around whereever she goes",
                    "flowers":"Ordinary Red roses",
                    "purse":"Nothing really except for food for her pets",
                    "receipt":"Bought one bag of cat food"},
        "michael" : {"headphones":"Black headphones by Sony",
                     "jacket":"You don't know the reason why Michael brought his Jacket but it was sure getting chilly in the house due to the air conditioner",
                     "reciept":"Unreadable receipt because it is all in black",
                     "chickenwings":"Seems like Michael had the time to go to the store, yummy chickenwings"},
        "edu" : {"box":"Just an empty box",
                 "phone":"Nothing... Edu has no internet connection so there is no way he could text anyone"},
        "johnathan" : {"reciept":"Bought orangejuice",
                       "orangejuice":"Orangejuice from the Diningroom",
                       "wallet":"A few photos of his mother, Sarra"},
        "matthew" : {"button":"Seems weird that he would have a button like this...",
                     "wallet":"A few credit cards",
                     "emptywaterbottle":"Just an emptywaterbottle",
                     "redcup":"Seems like Matthew does drink afterall",
                     "phone":"It seems odd that he would have Crystal's phone..."},
        "amanda" : {"bracelet":"A red bracelet that matches the colour of her hair",
                    "phone":"Her phone was dead so it was no use in investigating it since it isn't useable"},
        "june" : {"dogtreats":"Dogtreats for her puppy",
                  "dogcollar":"It seems that the puppy's name was Jack",
                  "necklace":"Purple Necklace that matches her eyes, green",
                  "purse":"Nothing in the beautiful flowered Purse"},
        "july" : {"dogshirt":"A nice red and blue dogshirt",
                  "purse":"Dog food and cosmetics were found in July's tiny purse",
                  "watch":"Black watch for time",
                  "phone":"Nothing interesting about Crystal found in this phone"},
        "julissa" : {"phone":"A recent message to Crystal asking where the party is located at",
                     "bag":"An old grocery bag",
                     "reciept":"Bought a bag of dogfood",
                     "dogtag":"It says Jack"},
        "puppy" : {"interact":"Bark Bark"},
        "jade" : {"interact":"Jade seems very busy and definitely needs privacy, maybe later"}

#the backyard,there'll be a little puppy which is june's

#There should be an option to talk to someone if you want to in the person_item selecion. This should reveal some backstory or something about their reason of coming to the party
    }







    #  Test Code
    while True:
        print(rooms.keys())
        room_choice = input("Which Room will you like to pick?: ")
        if room_choice in rooms:
            print("\n\n\n\n\n\n",rooms[room_choice])
            people_choice = input("Which person would you like to look into?: ")
            if people_choice in people_items:
                print("\n\n\n\n\n\n",people_items[people_choice])
                item_choice = input("Which item would you like to investigate?: ")
                if item_choice in people_items[people_choice]:
                    print("\n\n\n\n\n\n\n",people_items[people_choice][item_choice])
                    input()
                else:
                    print("\n\n\n\n\n","Please redo your choices again")
                    input()
                    pick2()
                if item_choice == "button":
                    return False
                if item_choice == "phone":
                    return False
