from cards import *

# Functions receive objects, not attributes contained within objects, as parameters.
# The attributes are called accordingly within each function.

def draw_card(Deck, Hand):
    newCard = Deck.deck.pop()
    Hand.hand.append(newCard)


def take_turn(Deck, Hand):
    print('Cards: | ' + ' | '.join(Hand.hand) + ' |')
    print('Total = ' + str(Hand.get_hand_value(Hand.hand)))
    choice = input('Hit or Stay?')

    # TODO: Test this section
    while choice.lower() != 'hit' or choice.lower() != 'stay':
        choice = input('Hit or Stay?')
    while choice.lower() == 'hit':
        draw_card(Deck.deck, Hand.hand)
        print('Cards: | ' + ' | '.join(Hand.hand) + ' |')
        print('Total = ' + str(Hand.get_hand_value(Hand.hand)))
        choice = input('Hit or Stay?')
    if choice.lower() == 'stay':
        print('Staying at ' + str(Hand.get_hand_value()))


def busted(Hand):
    bust = False
    if Hand.get_hand_value(Hand.hand) > 21:
        bust = True
    return bust


def main():  # This will be the game loop
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
        take_turn(gameDeck, playerHand)


if __name__ == "__main__":  # Initiate main loop when run as script
    main()
