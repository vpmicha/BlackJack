from ast import Pass
from cards import deck
import random
import sys

def main():
    hands, player_cards, dealer_cards = initial_deal(deck)
    print(hands)
    while True:
        check_winV = check_win(player_cards, dealer_cards)
        next_move = next_move(cards)


def initial_deal(cards):
    card1 = random.choice(list(cards))
    value1 = deck.pop(card1)
    card2 = random.choice(list(cards))
    value2 = deck.pop(card2)
    card3 = random.choice(list(cards))
    value3 = deck.pop(card3)
    card4 = random.choice(list(cards))
    value4 = deck.pop(card4)
    return f'Player: {value1+value3} ==> {card1}({value1}) / {card3}({value3})  || Dealer: {value2} ==> {card2}({value2}) / Hidden', [value1, value3], [value2, value4]

def check_win(cards1, cards2):
    if sum(cards1) == 21 and sum(cards2) == 21:
        return True
    elif sum(cards1) == 21:
        return True
    elif sum(cards2) == 21:
        return True
    elif sum(cards1) > 21:
        return 'Player Lost'
    elif sum(cards2) > 21:
        return 'Dealer Lost'
    else:
        Pass
        

main()