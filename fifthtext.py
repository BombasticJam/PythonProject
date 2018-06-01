def pick2():
    room_choice = []
    rooms = {
            "bedroom" : "Liliana\nBriana\nKevin\nHoward",
            "kitchen" : "Nicole\nHenry\nArnold\nAdrian\nCrystal",
            "partyroom" : "Pamela\nLaisha\nArleen\nAndrew\nMishael\nJohn\nDaniel\nLanaya\nNatalie\nJacob",
            "diningroom" : "Michael\nEnrico\nEdu\nJohnathan\nMatthew\nAmanda",
            "backyard" : "June\nJuly\nDawn\nJulissa\nPuppy",
            "bathroom" : "Jade"
    }

    people_items = {
        "liliana" : "wallet\ndice\nreciept\nmonopoly_money",
        "briana" : "purse\nreceipt\nphone\nmonopoly_money",
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
        "edu" : "box\nphone"
        "johnathan" : "reciept\norangejuice\nwallet",
        "matthew" : "button\nwallet\nemptywaterbottle\nredcup\nphone",
        "amanda" : "braclet\nphone\npurse",
        "june" : "dogtreats\ndogcollar\nflowers\nnecklace",

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
        "reciept" : "Bought 4 bags of fruit and a limited edition monopoly gameboard",
        "nmonopoly_money" : "1000 monopoly credits"
    }

    briana = {
    "purse" : ""
    }

    kevin = {
    "watch" : "",

    }


    #  Test Code
    print(rooms["bedroom"])
    print(people_items["kevin"])
    print(kevin["watch"])

pick2()
