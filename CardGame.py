from Player import *


class CardGame:
    def __init__(self, player: str, player_num_cards: int, player2: str, player2_num_cards: int):
        if type(player) != str:
            raise TypeError("Argument player must be str")
        if type(player2) != str:
            raise TypeError("Argument player must be str")
        if type(player_num_cards) != int:
            raise TypeError("Argument player must be int")
        if type(player2_num_cards) != int:
            raise TypeError("Argument player must be int")
        self.my_deck = DeckOfCards()
        self.player = Player(player, player_num_cards)
        self.player2 = Player(player2, player2_num_cards)
        self.new_game()
        # self.my_deck = DeckOfCards()

    def new_game(self):
        """Shuffles the deck and distributes random cards to a players hand"""
        self.my_deck.cards_shuffle()
        self.player.set_hand(self.my_deck)
        self.player2.set_hand(self.my_deck)

    def get_winner(self):
        """Checks which player has more cards and prints the appropriate message"""
        if len(self.player.player_deck) == len(self.player2.player_deck):
            return print("It's a tie")
        elif len(self.player.player_deck) > len(self.player2.player_deck):
            print(f'{self.player.playername} is the winner!')
            return True
        else:
            print(f'{self.player2.playername} is the winner!')
            return False