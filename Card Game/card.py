import random

class Card:
    """A classic playing card. For this program, Ace is 1, Jack is 11, Queen is 12, and King is 13.

    The responsibility of Card is to keep track of the card facing up and the next card which is unknown.

    Attributes:
        value (int): The number of on a card.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)