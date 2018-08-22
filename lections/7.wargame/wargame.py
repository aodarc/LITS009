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



# Game helpers
def players_have_cards():
    return player1_hand.stack and player2_hand.stack

def get_game_winner():
    if player1_hand.stack:
        return player1_hand
    elif player2_hand.stack:
        return player2_hand
    else:
        return None

def play_round(player1, player2):
    ''' Main game logic method'''
    round_winner = None
    player1.shuffle()
    player2.shuffle()

    print('='*10)
    player1.deal_to_deck(table)
    print("card 1 {}".format(table.stack[-1]))
    player2.deal_to_deck(table)
    print("card 2 {}".format(table.stack[-1]))

    wait = input("press enter")

    def even_el(el):
        '''check, if the element is in even position(index in array 1,3,5... )'''
        return table.stack.index(el)%2

    def odd_el(el):
        ''' oposite to even el. indexes are 0,2,4...'''
        return not even_el(el)

    # here we calculate sum of each players cards. Based on that theyr'e on one stack
    # and odd cards are player1, and even cards are player2 (starting from 0)
    # reduce here is used only as example.
    # better to use would be sum(), or list comprehensions
    player1_sum = reduce(lambda acc,x: acc+x,
                    map(lambda card: card.value,
                        filter(odd_el,table.stack)))
    player2_sum = reduce(lambda acc,x: acc+x,
                    map(lambda card: card.value,
                        filter(even_el,table.stack)))

    print ("{} vs {}".format(player1_sum, player2_sum))
    if player1_sum > player2_sum:
        print("round won: p1")
        round_winner = player1
    elif player1_sum < player2_sum: 
        print("round won: p2")
        round_winner = player2
    elif players_have_cards():
        print("draw")
        round_winner = play_round(player1, player2)
    else:
        round_winner = get_game_winner()

    return round_winner

# Deal cards to players
while main_deck.stack:
    main_deck.deal_to_deck(player1_hand) 
    main_deck.deal_to_deck(player2_hand) 

# play unless no cards left
while players_have_cards():
    round_winner = play_round(player1_hand, player2_hand)
    # give cards from table to player
    table.deal_to_deck(round_winner, len(table.stack))

print('*'*10)
if player1_hand.stack:
    print("player 1 wins!")
else:
    print("player 2 wins!")

print('*'*10)
