import random

start_hand = 7
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

class Card:

    def __init__(self, ):
        self.name = "card"

    def __str__(self):
        return self.name

    def get_name(self):
        print(self.name)

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


main_deck = Deck()



class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        for i in range(start_hand):
            self.hand.append(main_deck.from_top())



# class Hand:
#     def __init__(self):


class Stable:
        pass

me = Player("Cam")
for h in me.hand:
    print(h)

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
