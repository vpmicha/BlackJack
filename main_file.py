from cards import deck
import random
import sys
import time

def main():
    while True:
        hands, player_cards, dealer_cards = initial_deal(deck)
        print(hands)
        while True:
            continuation = input('Hit or Stand? [H]/[S]:').lower().strip()
            if continuation == 'h':
                check_winV = check_win(player_cards)
                if check_winV == 'Player ACED':
                    break
                print(next_move_player(deck, player_cards))
            elif continuation == 's':
                time.sleep(0.5)
                print(f'Hidden Card --> {dealer_cards[-1]} || Total Sum --> {sum(dealer_cards)}')
                break
        while True:
            check_winV = check_winD(dealer_cards)
            if check_winV == 'Dealer Lost':
                break
            elif check_winV == 'Dealer Won':
                break
            elif check_winV == 'STAND':
                print(f'Total Sum --> {sum(dealer_cards)}')
                break
            elif check_winV == 'HIT':
                print(next_move_dealer(deck, dealer_cards))
                time.sleep(0.5)

        if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) <= 21:
            print('Dealer Wins!')
        elif sum(dealer_cards) == sum(player_cards):
            print('Push!')

        else:
            print('Player Won!')
        print(deck)

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
        return 'Player ACED'
    elif sum(cards1) > 21:
        return 'Player EXCEEDED'
    else:
        return f'{sum(cards1)}. Do you want to continue?'

def check_winD(cards2):
    if sum(cards2) == 21:
        return 'Dealer ACED'
    elif sum(cards2) > 21:
        return 'Dealer EXCEEDED'
    elif sum(cards2) < 17:
        return 'HIT'
    elif sum(cards2) >= 17:
        return 'STAND'

def next_move_player(bj_deck, p_cards):
    next_card = random.choice(list(bj_deck))   
    p_cards.append(bj_deck[next_card])
    return f'Player drew: {next_card}. Players Cards: {sum(p_cards)}'

def next_move_dealer(bj_deck, d_cards):
    next_card = random.choice(list(bj_deck))   
    d_cards.append(bj_deck[next_card])
    return f'Dealer drew: {next_card}. Dealer Cards: {sum(d_cards)}'
    
main()