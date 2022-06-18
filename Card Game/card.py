import random

class Card:
    """A classic playing card. For this program, Ace is 1, Jack is 11, Queen is 12, and King is 13.

    The responsibility of Card is to keep track of the card facing up and the next card which is unknown.

    Attributes:
        value (int): The number of on a card.
    """

    def __init__(self, value=None):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        if value is None:
            value = random.randint(1,13)
        self.value = value
    