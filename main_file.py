from ast import Pass
from cards import deck
import random
import sys

def main():
    hands, cards = initial_deal(deck)
    print(hands)
    check_winV = check_win(cards)


def initial_deal(cards):
    card1 = random.choice(list(cards))
    value1 = deck.pop(card1)
    card2 = random.choice(list(cards))
    value2 = deck.pop(card2)
    card3 = random.choice(list(cards))
    value3 = deck.pop(card3)
    card4 = random.choice(list(cards))
    value4 = deck.pop(card4)
    return f'Player: {value1+value3} ==> {card1}({value1}) / {card3}({value3})  || Dealer: {value2} ==> {card2}({value2}) / Hidden ==> ', [value1, value2, value3, value4]

def check_win(list):
    if list[0] + list[2] < 21 and list[1] + list[3] < 21:
        pass
    elif list[0] + list[2] < 21 and list[1] + list[3] == 21:
        pass
    elif list[0] + list[2] == 21 and list[1] + list[3] < 21:
        pass
    elif list[0] + list[2] == 21 and list[1] + list[3] == 21:
        pass

    return 'a'


main()