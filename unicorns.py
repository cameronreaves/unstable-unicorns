import random

#set rules
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

    def count_uni_stable(self):
        count = 0
        for s in self.my_stable.stable:
            if str(s) == "Unicorn":
                count += 1
        return count

    def check_and_take(self, card_name):
        for i in range(len(self.hand)):
            if self.hand[i].get_name() == card_name:
                card =  self.hand[i]
                del self.hand[i]
                return card

# Stable

class Stable:
    def __init__(self):
        self.stable = []

main_deck = Deck()
main_trash = Trash()
me = Player("Cam")


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
