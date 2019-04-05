from random import shuffle  # By doing this, shuffle can only be called within objects created from this module

class Deck:

    def __init__(self):
        self.deck = []  # Write this here so it's specific to the object

    def build(self, deck):  # Populates a deck list and shuffles it
        suit = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in range(5):
            deck.extend(suit)
        shuffle(deck)

class Hand:

    def __init__(self):
        self.hand = []  # Contains cards as strings

    def get_card_value(self, card):  # Returns the numerical value of a card
        cardValues = {
            'AL': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'AH': 11
        }
        return cardValues[card]

    def get_hand_value(self, hand):
        currentHand = sorted(hand)  # Create new temporary list to avoid changing hand
        currentValue = 0  # Create new temporary variable to avoid changing handValue
        for card in currentHand:
            if card != 'A':
                currentValue += self.get_card_value(card)
            else:
                if currentValue > 10:  # Ace can no longer equal 11 without causing bust
                    currentValue += self.get_card_value('AL')
                elif currentValue <= 10:  # Ace should be counted as higher when advantageous
                    currentValue += self.get_card_value('AH')
        return currentValue
