from cards import *


def draw_card(deck, hand):
    newCard = deck.pop()
    hand.append(newCard)


def main():  # This will be the game loop
    gameDeck = Deck()
    playerHand = Hand()
    dealerHand = Hand()

    gameDeck.build(gameDeck.deck)
    draw_card(gameDeck.deck, playerHand.hand)


if __name__ == "__main__":  # Initiate main loop when run as script
    main()
