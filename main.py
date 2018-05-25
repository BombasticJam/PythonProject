import secondtext as st
import thirdtext as tt

class Game:
  def pause():
    input()



  def __init__(self):
    self.state = [""]
    self.player = []
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

  def secondmid(self):
      s1 = ("Crystal:'Please... help'")
      print(s1)
      input()
      s2 = ("Crystal:'It hurts.. inside'")
      print(s2)
      input()

            #This code below will break but I will soon fix it
      s3 = ((self.player, " : "), "'What happened to you?'").join()
      print(s3)
      input()
      s4 = ((self.player, ": "), "'Did you fall or...'").join()
      print(s4)
      s5 = ("Crystal: 'No, i think it something was in my drink'")
      print(s5)
      input()
      s6 = ("Crystal: 'I just can't s.. -*Cough*-'")
      print(s6)
      input()
      s7 = ((self.player, ": "), "Just hold on tight love, I'll get some help quick")
      print (s7)
      input()
      s8 = ("Crystal: 'No, don't leave -*Cough*- my side please.. I'm scared")
      print(s8)
      input()
      s9 = "You see Crystal move side to side as she struggles to breath"
      print(s9)
      input()
      s10 = "You try to perform CPR on her with all your might"
      print(s10)
      s11 = ("You soon fail and try to call for help")
      print(s11)
      input()
a = Game()
a.start()
print(st.mid())
print(a.secondmid(player))
