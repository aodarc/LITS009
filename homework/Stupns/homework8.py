from functools import reduce
from random import shuffle
class Card(object):
    SUITS = ['hearts', 'spades', 'diamonds', 'clubs'] 

    def __init__(self, value, suit):
        if suit not in Card.SUITS:
            raise Exception('no such suit')
        self.suit = suit
        self.value = value

    def is_red(self):
        if self.suit in ['hearts', 'diamonds']:
            return True
        else:
            return False

    def formatted_value(self):
        if self.value == 14: return 'ace'
        elif self.value == 13: return 'king'
        elif self.value == 12: return 'queen'
        elif self.value == 11: return 'jack'
        else: return self.value


    def __repr__(self):
        return "{} of {}".format(self.formatted_value(), self.suit)


class CardDeck:
    def __init__(self, stack=None):
        if stack is not None:
            self.stack = stack
        else:
            self.stack = []
            self.populate()

    def populate(self):
        for suit in Card.SUITS:
            for value in range(2,15):
                card = Card(value, suit)
                self.stack.append(card)

    def shuffle(self):
        shuffle(self.stack)

    def deal(self, amount=1):
        acc=[]
        for i in range(amount):
            acc.append(self.stack.pop())
        return acc

    def deal_to_deck(self, deck, amount=1):
        deck.stack += self.deal(amount)


    def __repr__(self):
        result = ""
        for card in self.stack:
            result+=card.__str__()+'\n'
        return result




# Game Logic:

main_deck = CardDeck()
main_deck.shuffle()
player1_hand = CardDeck([])
player2_hand = CardDeck([])

table = CardDeck([])

print(main_deck)