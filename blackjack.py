import random
import time

def create_deck():
    """Set up the deck and shuffle."""

    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_values = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9,
                   '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    global deck
    deck = [(card, (suit, card_values[card])) for card in cards for suit in suits]

    for i in range(3):
        random.shuffle(deck)

    return deck

def welcome():
    """Get name and age, welcome user if over 18."""
    message = 'What is your name? '
    name = input(message)

    while True:
        message = f"Hello, {name.title()}, how old are you? "
        try:
            age = int(input(message))
        except ValueError:
            print('\nThat is not a valid response.')
            continue

        if age < 18:
            print('\nSorry, you are too young to play this game.')
            break
        else:
            prompt = '\nDo you know the rules of blackjack? (Y/N) '
            yes_no = input(prompt)
            if yes_no.upper() == 'N':
                explain_game()
            else:
                play_game()


def explain_game():
    """Explain the rules of blackjack."""
    rules = '\n1. Blackjack starts with players making bets.'\
            '\n2. Dealer deals 2 cards to the players and two to himself '\
            '(1 card face up, the other face down).'\
            '\n3. Blackjack card values: All cards count their face value in '\
            'blackjack. Picture cards count as 10 and the ace can count as '\
            'either 1 or 11. Card suits have no meaning in blackjack. '\
            'The total of any hand is the sum of the card values in the hand'\
            '\n4. Players must decide whether to stand, hit or split.'\
            '\n5. The dealer acts last and must hit on 16 or less and stand on 17 through 21.'\
            '\n6. Players win when their hand totals higher than dealer’s hand, '\
            'or they have 21 or less when the dealer busts (i.e., exceeds 21).'
    print(rules)

    ready = input('\nAre you ready to play? (Y/N) ')
    if ready.upper() == 'Y':
        play_game()
    else:
        explain_game()

def play_game():
    """Start the game."""
    player_cards = []
    dealer_cards = []
    deck = create_deck()

    # Deal two cards to player and one to dealer (alternating)
    player_cards.append(deck.pop())
    dealer_cards.append(deck.pop())
    player_cards.append(deck.pop())

    # Show cards
    pc1 = player_cards[0][1][1]
    pc2 = player_cards[1][1][1]

    dealer_hand = dealer_cards[0][1][1]
    player_hand = pc1 + pc2

    while True:
        print(f'\nYou have {player_hand} and dealer has {dealer_hand}.')
        if player_hand == 21:
            print('Blackjack!')
            break
        else:
            hit_stick = input('\nWould you like to hit (H) or stick (S)? ')
            if hit_stick.upper() == 'H':
                new_card = deck.pop()
                player_cards.append(new_card)
                player_hand += new_card[1][1]
                if player_hand > 21:
                    print(f'{player_hand}, bust. You lose!')
                elif player_hand == 21:
                    print('21!')
                    break
                else:
                    continue
            elif hit_stick.upper() == 'S':
                # Dealer turn
                while True:
                    new_d_card = deck.pop()
                    dealer_cards.append(new_d_card)
                    dealer_hand += new_d_card[1][1]
                    print(f'\nDealer has {dealer_hand}')
                    if dealer_hand < 17:
                        print('Taking another card...')
                        time.sleep(2)
                        continue
                    elif dealer_hand > 21:
                        print('Dealer bust, you win!')
                        break
                    else:
                        if player_hand > dealer_hand:
                            print(f'You win {player_hand} > {dealer_hand}.')
                        elif player_hand < dealer_hand:
                            print(f'You lose {player_hand} < {dealer_hand}.')
                        elif player_hand == dealer_hand:
                            print(f'Stand {player_hand} = {dealer_hand}.')
                        break
            else:
                print('\nThat is not a valid response.')
                continue
        break

    play_again = input('\nWould you like to play again? (Y/N) ')
    if play_again.upper() == 'Y':
        play_game()
    else:
        print('Thank you for playing!')

welcome()
