from card import Card

class Director:
    """A person who directs the game, the dealer.
    
    The responsibility of a Director is to control the steps of the game.
    
    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is still going.
        score (int): The score for one round.
        total_score (int): The score for the whole game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.continue_playing = True
        self.total_score = 300
        self.guess = ""
    
    def start_game(self):
        """Starts the game in a loop that runs until no longer playing.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.continue_playing:
            card1 = Card()
            print(f"The card is: {card1.value}")
            self.get_input()
            card2 = Card()
            print(f"Next card was: {card2.value}")
            self.score_game(card1.value, card2.value)
            print(f"Your score is: {self.total_score}")
            self.replay() 

    def get_input(self):
        """Ask the user if they think the next card is higher or lower.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guess = input("Higher or lower? [h/l] ")
    
    def score_game(self, card1, card2):
        """Updates the player's score.
        
        Args:
            self (Director): an instance of Director.
        """
        if not self.continue_playing:
            return

        if card1 > card2 and self.guess == "h":
            self.score = 75
            self.total_score -= self.score
        elif card1 < card2 and self.guess == "l":
            self.score = 75
            self.total_score -= self.score
        elif card1 > card2 and self.guess == "l":
            self.score = 100
            self.total_score += self.score
        elif card1 < card2 and self.guess == "h":
            self.score = 100
            self.total_score += self.score
        

    def replay(self):
        """Asks player if they would like to play again.
        
        Args:
            self (Director): an instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        self.continue_playing = (play_again == "y")