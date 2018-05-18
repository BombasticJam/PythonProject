 import secondtext as st

class Game:

  player = []

  def __init__(self):
    self.state = [""]
    self.game_over = False

  def __repr__(self):
    return 'Game ({})'.format(self.state)

  def __str__(self):
    return self.state

#    person = input('Enter your name: ')
#    print('Hello {}!'.format(person))

  def start(self):
    try:
        person = input("Hello,\nWelcome to my Game!\nPlease Enter Your Name:  ").format(self.player)
        print(person, "...").join(format(person))
    except AttributeError:
        st.pause()
        welcome_1 = ("So its {} huh,\nWhat a Great Name of yours").format(person)
        print(welcome_1)
        st.pause()
        welcome_2 = ("You should really get going {},\nYou have a party and guests waiting to be attended").format(person)
        print(welcome_2)
        st.pause()
        lots_of_spaces = ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(lots_of_spaces)
a = Game()
a.start()
print(st.mid())
