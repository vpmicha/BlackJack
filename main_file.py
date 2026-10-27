from cards import deck
import random
import sys

def main():
    hands, player_cards, dealer_cards = initial_deal(deck)
    print(hands)
    while True:
        check_winV = check_win(player_cards)
        print(next_move(deck, cards))
        continuation = input('Hit or Stand? [H]/[S]:').lower().strip()
        if continuation == 'H':
            Pass
        elif continuation == ''


def initial_deal(deck):
    card1 = random.choice(list(deck))
    value1 = deck.pop(card1)
    card2 = random.choice(list(deck))
    value2 = deck.pop(card2)
    card3 = random.choice(list(deck))
    value3 = deck.pop(card3)
    card4 = random.choice(list(deck))
    value4 = deck.pop(card4)
    return f'Player: {value1+value3} ==> {card1}({value1}) / {card3}({value3})  || Dealer: {value2} ==> {card2}({value2}) / Hidden', [value1, value3], [value2, value4]

def check_win(cards1):
    if sum(cards1) == 21:
        return 'Player Won'
    elif sum(cards1) > 21:
        return 'Player Lost''
    else:
        return f'{sum(cards1)}. Do you want to continue?'

def next_move(bj_deck, p_cards):
    next_card = random.choice(list(bj_deck))   
    p_cards.append(bj_deck[next_card])
    return f'Player drew: {next_card}. Players Cards: {sum(p_cards)}'

main()