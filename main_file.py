from cards import deck
import random
import sys

def main():
    hands, cards = initial_deal(deck)
    print(hands)
    check_win = check_win(cards)


def initial_deal(cards):
    card1 = random.choice(list(cards))
    value1 = deck.pop(card1)
    card2 = random.choice(list(cards))
    value2 = deck.pop(card2)
    card3 = random.choice(list(cards))
    value3 = deck.pop(card3)
    card4 = random.choice(list(cards))
    value4 = deck.pop(card4)
    return f'Player: {card1}({value1}) / {card3}({value3}) ==> {value1+value3} || Dealer: {card2}({value2}) / Hidden ==> {value2}', [value1, value2, value3, value4]

main()