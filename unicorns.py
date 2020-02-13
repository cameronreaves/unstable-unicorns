import random

#set rules
start_hand = 3
card_types = [1, 2, 3, 4, 5]
size = 50

def type_switch(argument):
    switcher = {
        1: Unicorn(),
        2: Instant(),
        3: Magic(),
        4: Upgrade(),
        5: Downgrade()
    }
    return(switcher.get(argument))



# Deck / Piles

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(size):
            type = random.sample(card_types, 1)
            self.deck.append(type_switch(type[0]))

    def from_top(self):
        return self.deck.pop()

    def to_deck(self,card):
        self.deck.insert(random.randint(0, len(self.deck)),card)

class Trash:
    def __init__(self):
        self.trash = []

    def from_top(self):
        return self.trash.pop()

    def to_trash(self,card):
        self.trash.insert(random.randint(0, len(self.trash)),card)

    def show_trash(self):
        for t in self.trash:
            print(t)


#   Cards

class Card:

    def __init__(self, ):
        self.name = "card"

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

class Unicorn(Card):
    def __init__(self):
        self.name = "Unicorn"

class Instant(Card):
    def __init__(self):
        self.name = "Instant"

class Magic(Card):
    def __init__(self):
        self.name = "Magic"

class Upgrade(Card):
    def __init__(self):
        self.name = "Upgrade"

class Downgrade(Card):
    def __init__(self):
        self.name = "Downgrade"

# Player

class Player:
    def __init__(self, name):
        self.hand = []
        self.my_stable = Stable()
        self.name = name
        for i in range(start_hand):
            self.hand.append(main_deck.from_top())

    def __str__(self):
        return self.name

    def draw_deck(self):
        self.hand.append(main_deck.from_top())

    def draw_trash(self):
        if len(main_trash.trash) > 0:
            self.hand.append(main_deck.from_top())
        else:
            print("Sorry there is no trash")

    def from_hand_to_deck(self,card):
        new = self.check_and_take(card)
        if new:
            main_deck.to_deck(new)
            return True
        else:
            return False

    def from_hand_to_trash(self,card):
        new = self.check_and_take(card)
        if new:
            main_trash.to_trash(new)
            return True
        else:
            return False

    def put_stable(self, card):
        new = self.check_and_take(card)
        if new:
            self.my_stable.stable.append(new)
            return True
        else:
            return False

    def show_hand(self):
        for h in self.hand:
            print(h)

    def get_hand(self):
        return self.hand

    def show_stable(self):
        for s in self.my_stable.stable:
            print(s)

    def check_stable(self):
        types = ["Unicorn", "Upgrade", "Downgrade"]
        u_count = 0
        up_count = 0
        down_count = 0
        for s in self.my_stable.stable:
            if str(s) == types[0]:
                u_count += 1
            elif str(s) == types[1]:
                up_count += 1
            else:
                down_count += 1
        counts = [u_count, up_count, down_count]
        return counts


#   goes through a players hand and looks for that card, deletes that card from the hand and then returns it
    def check_and_take(self, card_name):
        for i in range(len(self.hand)):
            if self.hand[i].get_name() == card_name:
                card =  self.hand[i]
                del self.hand[i]
                return card

    def steal_my_from_stable(self,card_name):
        if len(self.my_stable.stable) > 0:
            for i in range(len(self.my_stable.stable)):
                if self.my_stable.stable[i].get_name() == card_name:
                    card = self.my_stable.stable[i]
                    del self.my_stable.stable[i]
                    main_trash.to_trash(card)
                    return True
        return False

    def instant_play(self):
        main_trash.to_trash(self.my_stable.stable.pop())

    def reduce_hand(self):
        limit = 3
        self.hand[0:limit]




# Stable

class Stable:
    def __init__(self):
        self.stable = []

main_deck = Deck()
main_trash = Trash()
players = []
#create players for the game
players.append(Player("Cam"))
players.append(Player("Naomi"))
run = True

# players[1].show_hand()
# print("\n")
# players[1].put_stable("Unicorn")
# players[1].show_stable()
# bool = players[1].steal_my_from_stable("Unicorn")
# if bool:
#     print("worked")
# else:
#     print("not famo")
# print("\n")
# players[1].show_stable()
# main_trash.show_trash()





# print("""
# Welcome to Unicorns!
# The Goal of the Game is to get X unicorns in your stable.
# Magic cards take away an opponent's unicorn from their stable 
# Upgrade cards give you an card each turn
# Downgrade cards reduce your opponents hand to 5 cards
# Instant cards block your opponents card that they just played
# """)
#
while(run):
#for each player in the game
    for i in range(len(players)):
        turn = True
        # makes sure that the player doesn't draw again if she inputs the wrong card name
        new_turn = True
        ##turn
        while(turn):
            ply = players[i]
            print("It's your turn,  " + str(ply))
            if new_turn:
                ply.draw_deck()
                for i in range(ply.check_stable()[1]):
                    print("Upgrade, drawing again!")
                    ply.draw_deck()
            print("\n HAND")
            ply.show_hand()
            print("\n STABLE")
            ply.show_stable()
            action = input("\n Type card name or type draw ----->  ")
            if action == "draw":
                ply.draw_deck()
            else:
                suc = ply.put_stable(action)
                if suc:
                    print("You played the " + action + " card to your stable")
                    if ply.check_stable()[2] > 0:
                        print("You have a downgrade card! Reducing your hand.")
                        ply.reduce_hand()
                    turn = False
                else:
                    print("Card not in your hand")
                    new_turn = False
        unis = ply.check_stable()
        if unis[0] > 2:
            print(str(ply) + " is the winner")
            run = False






# print("Hello")
# print(me.check_if_card("Unicorn"))
# me.show_hand()
# print("\n")
# main_trash.show_trash()
# print("\n")
# me.from_hand_to_trash()
# me.show_hand()
# print("\n")
# main_trash.show_trash()

# print("vv")
#
# me.put_stable()
# me.put_stable()
#
# me.show_stable()
#
# print(me.count_uni_stable())

# deck = Deck()
#
# for d in deck.deck:
#     d.get_name()
#
# print(deck.off_top())
#
# for d in deck.deck:
#     d.get_name()
#
# print(deck.put_back(Unicorn()))
#
# for d in deck.deck:
#     d.get_name()
# # bill = Card()
# # fred = Unicorn()
#
# bill.get_name()
# fred.get_name()
