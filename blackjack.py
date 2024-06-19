import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def display_board(player_hand, dealer_hand, player_value, dealer_value, game_over=False):
    print("\nPLAYER'S HAND:")
    for card in player_hand.cards:
        print(card)
    print(f'Total Value: {player_value}\n')

    print("DEALER'S HAND:")
    if not game_over and len(dealer_hand.cards) == 2:
        print(dealer_hand.cards[0])
        print("Hidden Card")
    else:
        for card in dealer_hand.cards:
            print(card)
    if game_over:
        print(f'Total Value: {dealer_value}')
    else:
        print("Total Value: ?\n")

def blackjack_game():
    deck = Deck()

    player_hand = Hand()
    dealer_hand = Hand()

    # Initial deal
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    player_value = player_hand.value
    dealer_value = dealer_hand.value

    display_board(player_hand, dealer_hand, player_value, dealer_value)

    while True:
        if player_hand.value == 21:
            print("Blackjack! You win!")
            break
        elif player_hand.value > 21:
            print("Bust! You lose!")
            break
        else:
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                player_hand.add_card(deck.deal_card())
                player_hand.adjust_for_ace()
                player_value = player_hand.value
                display_board(player_hand, dealer_hand, player_value, dealer_value)
            elif choice == 's':
                break
            else:
                print("Invalid input! Please enter 'h' to hit or 's' to stand.")

    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.adjust_for_ace()
        dealer_value = dealer_hand.value

    display_board(player_hand, dealer_hand, player_value, dealer_value, game_over=True)

    if player_hand.value > 21:
        print("Player busts! Dealer wins!")
    elif dealer_hand.value > 21:
        print("Dealer busts! Player wins!")
    elif player_hand.value > dealer_hand.value:
        print("Player wins!")
    elif player_hand.value < dealer_hand.value:
        print("Dealer wins!")
    else:
        print("It's a push!")

if __name__ == "__main__":
    blackjack_game()