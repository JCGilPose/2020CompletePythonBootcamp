import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        cards_in_deck = 'This deck contains:\n'
        for card in self.deck:
            cards_in_deck += (card.__str__() + '\n')
        return cards_in_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Please place your bet. How many chips do you wager? '))
        except ValueError:
            print('Please enter an integer value.')
        else:
            if chips.bet > chips.total:
                print("Sorry, you only have:", chips.total)
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's': ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer's turn.")
            playing = False
            break # Exiting loop.
        else:
            print("Sorry, wrong input.")
            continue


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

    
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Players busts! Dealer wins!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts! Player wins!")
    chips.win_bet()

    
def dealer_wins(player, dealer,
                chips):
    print("Dealer wins!")
    chips.lose_bet()

    
def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('\nWelcome to BlackJack!\n\nGet as close to 21 as you can without going over!')
    print('Dealer hits until she reaches 17.\nAces count as 1 or 11.\n')
    
    # Create & shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Set up the player's hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Set up the dealer's hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the player's chips; default = 100
    player_chips = Chips()  
    
    # Player places bet
    take_bet(player_chips)
    
    # Show all cards except one dealer card
    show_some(player_hand, dealer_hand)
    
    while playing:  # variable from hit_or_stand function
        
        # Prompt player
        hit_or_stand(deck, player_hand) 
        
        # Show all cards except one dealer card
        show_some(player_hand, dealer_hand)  
        
        # If player gone over 21: BUST!
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break        


    # If player not gone bust, dealer's turn 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)    
    
        # Show all cards
        show_all(player_hand, dealer_hand)
        
        # Check for winner
        # Dealer bust == player wins
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        # Dealer closer to 21 and wins
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        # Player closer to 21 and wins
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        # Tie -- Let's push!
        else:
            push(player_hand,dealer_hand)        
    
    # Chips total update
    print("\nPlayer's chips total stands at", player_chips.total)
    
    # Another game?
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
