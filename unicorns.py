

class Deck:
    def __init__(self):
        size = 50
        self.deck = []
        for i in range(size):
            self.deck.append(Card())

 #   def deal(self, n):
 #      return random.sample(self.deck, n)

class Pile(Deck):
    pass

class Trash(Deck):
    pass

class Card:

    def __init__(self, ):
        self.type = "hello"

    def hey(self):
        print(self.message)

class Unicorn(Card):
    pass

class Instant(Card):
    pass

class Magic(Card):
    pass

class Upgrade(Card):
    pass

class Downgrade(Card):
    pass

class Player:
    pass

class Hand:
        pass

class Stable:
        pass



deck = Deck()

for d in deck.deck:
    d.hey()