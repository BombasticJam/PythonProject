def pick2():
    rooms = {
            "bedroom" : ["Liliana","Briana", "Kevin", "Howard"],
            "kitchen" :"Nicole\nHenry\nArnold\nAdrian\nCrystal",
            "partyroom" : "Pamela\nLaisha\nArleen\nAndrew\nMishael\nJohn\nDaniel\nLanaya\nNatalie\nJacob",
            "diningroom" : "Michael\nEnrico\nEdu\nJohnathan\nMatthew\nAmanda",
            "backyard" : "June\nJuly\nDawn\nJulissa\nPuppy",
            "bathroom" : "Jade"
    }

    people_items = {
        "liliana" : ["wallet","dice","reciept","monopoly_money"],
        "briana" : "purse\nreceipt\nphone\nheadphones\nmonopoly_money",
        "kevin" : "watch\npencil\nnotebook\nheadphones\nmonopoly_money",
        "howard" : "wallet\nrepiept\npaper\nmonopoly_money",
        "nicole" : "toothpick\nempty_water_bottle\npurse\nbracelet",
        "henry" : "keychain\nredcup\nwallet\nmintgum\ncigarettes",
        "arnold" : "bandana\nwallet\nwatch\nmatches\nphone",
        "adrian" : "dogtag\npurse\nwallet\nnametag\npaper\nphone",
        "crystal" : "bloodypieceofpaper\npurse\ncrystalnecklace\nbracelet\nbody",
        "pamela" : "necklace\nbracelet\npen\nwatch\npurse\nphone",
        "laisha" : "deckofcards\nlipstick\npurse\nlolipop\nheadphones\nphone",
        "arleen" : "waterbottle\nsmallbackpack\ncosmetic\nbubblegum\nphone",
        "andrew" : "headband\nbeer\nphone\nkeys\nglasses",
        "mishael" : "bookmark\nseedpackets\ncard\nphone\nmarbles",
        "john" : "cdplayer\ncddisk\nwallet\ncandybar\nredcup",
        "daniel" : "cigarettes\ncase\nbusinesscard\nreceipt",
        "lanaya" : "kitten\nhamster\nflowers\npurse\nreceipt",
        "natalie" : "journal\nphone\nheadphones\npencil",
        "jacob" : "painkillers\nnecklace\nwallet\nbadge",
        "michael" : "headphones\njacket\nreciept\nchickenwings",
        "enrico" : "lotion\nnapkin\ncarkeys\nmarkers",
        "edu" : "box\nphone",
        "johnathan" : "reciept\norangejuice\nwallet",
        "matthew" : "button\nwallet\nemptywaterbottle\nredcup\nphone",
        "amanda" : "braclet\nphone\npurse",
        "june" : "dogtreats\ndogcollar\nflowerhat\nnecklace\npurse",
        "july" : "dogshirt\npurse\nwatch\nphone\ncandybits\nflowerhat",
        "dawn" : "redball\nglasses\nphone\nwaterbottle\nflowerhat",
        "julissa" : "phone\nbag\nreciept\ndogtag",
        "puppy" : "talk",
        "jade" : "interact"

#crystal will have a button which will be the trophy of the murder (The murder will have to contain her button)  Crystal's purse's goods have been stolen so her purse will contain nothing
#Pamela will have similar items that crystal will have because they are best friends
#maybe the winner will be calling crystal's phone
#pamela will have stuff in her purse such as a lolipop and otherthings
#arleen will carry a backpack that will contain food
#laisha got a lolipop from pamela (also great friends with pamela)
#Mishael's card is an ace of heart
#Mishael's marbles will be blue and green
#Natalie's journal will hold anytyhing bts
#Jacob's badge will represent his internship in the police academy
#Michael would carry a jacket even though it is very hot outside but ac is present
#Michael's chicken wing will output text such as yum
#Edu's box will be on the floor but you ask him to open it but he says no so you just move it and you feel something heavy but ignore it


#the backyard,there'll be a little puppy which is june's

#There should be an option to talk to someone if you want to in the person_item selecion. This should reveal some backstory or something about their reason of coming to the party
    }




    liliana = {
        "wallet" : "As you look into her wallet, something fell out of it which made you muffle 'Deja vu' as you picked it up and looked at it. It was a white piece of plastic which looked like a gum wrapper. You put the gum wrapper into your pocket and search the wallet thorough but found nothing but credit cards.",
        "dice" : "Just some plain old white dice, nothing to be interested in",
        "reciept" : "Bought 4 bags of fruit (Who needs 4 bags of fruit...) and a limited edition monopoly gameboard",
        "nmonopoly_money" : "1000 monopoly credits"
    }

    briana = {
    "purse" : "As soon as Briana handed her purse to you, you looked in it and found absolutley nothing unusual present so you give it back to her",
    "reciept" : "Bought 1 bag of chips (Probably for the party), two liters of soda (Also for the party), and new headphones",
    "phone" : "She doesn't seem to want you to look into her phone so you put it back into her possesion",
    "headphones" : "that"
    }

    kevin = {
    "watch" : "",

    }


    #  Test Code

    print("\n\nbedroom\nkitchen\npartyroom\ndiningroom\nbackyard\nbathroom")
    room_choice = input("Which Room will you like to pick?: ")
    if room_choice in rooms:
        print("\n\n\n\n\n\n",rooms[room_choice])
        people_choice = input("Which person would you like to look into?: ")
        if people_choice in people_items:
            print("\n\n\n\n\n\n",people_items[people_choice])
            item_choice = input("Which item would you like to investigate?: ")
            if people_choice in item_choice:
                print("\n\n\n\n\n\n", people_choice[item_choice])











pick2()
