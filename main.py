import secondtext as st

class Game:

  def pause():
    input()

  bedroom = "bedroom"
  kitchen = "kitchen"
  party_room = "partyroom"
  dining_room = "diningroom"
  backyard = "backyard"
  bathroom = "bathroom"

  rooms = [bedroom, kitchen, party_room, dining_room, backyard, bathroom]

  henry = "henry"
  liliana = "liliana"
  joshua = "joshua"
  aaron = "aaron"
  todd = "todd"
  bandana = "bandana"
  gumwrappers = "gumwrappers"

  people_in_rooms = {
    bedroom:henry, kitchen:liliana, party_room:joshua, backyard: aaron, bathroom:todd
  }

  wallet_h = "*You see a picture of Henry's dog, stacy*"
  cigarettes_l = "*I never knew that Liliana smoked, nor did I know she had enough money to buy any due to the loans she has been stacking up for her so on 'College Fees'*"


  people_items = {
    henry:wallet_h, liliana:cigarettes_l, joshua:bandana, aaron:gumwrappers
  }





  wallet_h = "*As you open the leather wallet, you see Henry's dog, Stacy, who just passed away recently"


  player = []

  def __init__(self):
    self.state = [""]
    self.game_over = False

  def __repr__(self):
    return 'Game ({})'.format(self.state)

  def __str__(self):
    return self.state

  def start(self):
    welcome_1 = input("Hello,\nWelcome to my Game!\nPlease Enter Your Name:  ").format[self.player]
    print(welcome_1)
    pause()
    welcome_2 = ("So its {} huh,\nWhat a Great Name of yours").format[self.player]
    print(welcome_2)
    pause()
    welcome_3 = ("You should really get going {},\nYou have a party and guests waiting to be attended").format[self.player]
    print(welcome_3)
    pause()
    lots_of_spaces = ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(lots_of_spaces)
a = Game()
a.start()
print(st.mid())
