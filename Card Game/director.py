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
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.total_score = 300

        for i in range(2):
            card = Card()
            self.cards.append(card)
    
    def start_game(self):
        """Starts the game in a loop that runs until no longer playing.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_input()
            self.update_game()
            self.show_outputs()
            self.replay() 

    def get_input(self):
        """Show the current cardn and ask the user if they think the next card is higher or lower.
        
        Args:
            self (Director): an instance of Director.
        """
        current_card = Card.draw(self)
        print(f"The card is: {current_card}")
        player_guess = input("Higher or lower? [h/l] ")
    
    def update_game(self):
        """Updates the player's score.
        
        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return

        for i in range(len(self.cards)):
            card = self.cards[i]
            card.draw()
            self.score += card
        self.total_score += self.score
    
    def show_outputs(self):
        """Displays the cards and the score. Also asks about the next card.
        
        Args:
            self (Director): an instance of Director.
        """
        if not self.is_playing:
            return

        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            
        print(f"Next card was: {card}")
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)

    def replay(self):
        """Asks player if they would like to play again.
        
        Args:
            self (Director): an instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        self.is_playing = play_again == "y"