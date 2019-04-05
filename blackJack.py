from cards import *


def draw_card(deck, hand):
    newCard = deck.pop()
    hand.append(newCard)


def busted(hand):
    bust = False
    if hand.get_hand_value(hand.hand) > 21:
        bust = True
    return bust


def main():  # This will be the game loop
    print('Starting Black Jack')

    # Initialize starting game state
    gameDeck = Deck()
    gameDeck.build(gameDeck.deck)

    playerHand = Hand()
    dealerHand = Hand()

    draw_card(gameDeck.deck, dealerHand.hand)
    draw_card(gameDeck.deck, playerHand.hand)
    draw_card(gameDeck.deck, dealerHand.hand)
    draw_card(gameDeck.deck, playerHand.hand)

    while busted(playerHand) == False and busted(dealerHand) == False:  # Main game loop


if __name__ == "__main__":  # Initiate main loop when run as script
    main()
