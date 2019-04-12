from cards import *
import time

# Functions receive objects as arguments. Their attributes and methods are called accordingly within each function.
# DO NOT pass attributes into functions, except when it is a function defined in another module.

def draw_card(Deck, Hand):
    newCard = Deck.deck.pop()
    Hand.hand.append(newCard)


def player_turn(Deck, Hand):
    print('Cards: | ' + ' | '.join(Hand.hand) + ' |')
    print('Total = ' + str(Hand.get_hand_value(Hand.hand)))
    print('Hit or Stay?')
    choice = input().lower()

    while choice != 'hit' and choice != 'stay':
        print('Hit or Stay?')
        choice = input().lower()

    if choice == 'hit':
        draw_card(Deck, Hand)
        if Hand.get_hand_value(Hand.hand) > 21:
            busted(Hand)
        else:
            player_turn(Deck, Hand)
    elif choice.lower() == 'stay':
        print('Staying at ' + str(Hand.get_hand_value(Hand.hand)))
        return Hand.get_hand_value(Hand.hand)  # Once the player is done hitting and hasn't busted, return score


def dealer_turn(Deck, Hand):
    print('Dealer shows: | ? | ' + ' | '.join(Hand.hand[1:]) + ' |')

    if Hand.get_hand_value(Hand.hand) < 17:
        print('Dealer decides to hit')
        time.sleep(1)
        draw_card(Deck, Hand)
        if Hand.get_hand_value(Hand.hand) > 21:
            busted(Hand)
        else:
            dealer_turn(Deck, Hand)

    elif Hand.get_hand_value(Hand.hand) >= 17:
        if 'A' not in Hand.hand:  # If the dealer has hit at least 17 without an Ace, they stay
            print('Dealer decides to stay')
            return Hand.get_hand_value(Hand.hand)
        elif Hand.hand.count('A') < 2:  # The dealer will be a bit risky if they have one Ace
            print('Dealer decides to hit')
            time.sleep(1)
            dealer_turn(Deck, Hand)
            if Hand.get_hand_value(Hand.hand) > 21:
                busted(Hand)
            else:
                print('Dealer decides to stay')
                dealer_turn(Deck, Hand)
        else:  # If the dealer has 2 or more aces at this point, it's a risk to hit again
            return Hand.get_hand_value(Hand.hand)


def busted(Hand):  # Handles events if player or dealer busts
    bust = False
    if Hand.get_hand_value(Hand.hand) > 21:
        bust = True
    return bust


def main():  # Game loop
    print('Starting Black Jack')

    # Initialize starting game state
    gameDeck = Deck()
    gameDeck.build(gameDeck.deck)

    playerHand = Hand()
    dealerHand = Hand()

    draw_card(gameDeck, dealerHand)
    draw_card(gameDeck, playerHand)
    draw_card(gameDeck, dealerHand)
    draw_card(gameDeck, playerHand)

    while busted(playerHand) == False and busted(dealerHand) == False:  # Main game loop
        # Player's turn
        print('Dealer shows: | ? | ' + ' | '.join(dealerHand.hand[1:]) + ' |')
        playerScore = player_turn(gameDeck, playerHand)
        dealerScore = dealer_turn(gameDeck, dealerHand)
        if playerScore > dealerScore:
            # TODO: Create win message
        elif playerScore < dealerScore:
            # TODO: Create lose message
        else:
            # TODO: Handle a tie

    if busted(playerHand) == True:
        play = ''
        while play.lower() != 'yes' and play.lower() != 'no':
            print('Bust! Play again?')
            play = input()
        if play.lower() == 'no':
            print('Game over. Thanks for playing!')
        elif play.lower() == 'yes':
            main()

if __name__ == "__main__":  # Initiate main loop when run as script
    main()
