from random import sample




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
        card_types = [1, 2, 3, 4, 5]
        size = 50
        self.deck = []
        for i in range(size):
            type = sample(card_types, 1)
            self.deck.append(type_switch(type[0]))


 #   def deal(self, n):
 #      return random.sample(self.deck, n)

class Pile():
    pass

class Trash(Deck):
    pass

class Card:

    def __init__(self, ):
        self.name = "card"

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

class Player:
    pass

class Hand:
        pass

class Stable:
        pass



deck = Deck()

for d in deck.deck:
    d.get_name()
# bill = Card()
# fred = Unicorn()
#
# bill.get_name()
# fred.get_name()
