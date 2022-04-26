from DeckOfCards import *

class Player:

    def __init__(self,playername:str,card_num:int=26):
        if card_num < 10 or card_num > 26:
            card_num = 26
        if type(card_num) != int:
            raise TypeError('Cards number must be int')
        if type(playername) != str:
            raise TypeError('Player name must be str')
        self.player_deck=[]
        self.playername=playername
        self.card_num=card_num


    def __str__(self):
        return f'Player deck :{self.player_deck}'


    def set_hand(self, deck:DeckOfCards):
        """Gets a full deck and adds cards to players hand based on num_cards"""
        if type(deck)!=DeckOfCards:
            raise TypeError('Deck must be DeckOfCards type')
        for i in range(self.card_num):
            deleted=deck.deal_one()
            self.add_card(deleted)


    def get_card(self):
        """Returns a random card from the players hand and removes it"""
        a=choice(self.player_deck)
        self.player_deck.remove(a)
        return a



    def add_card(self,card:Card):
        """Adds a card to a players hand"""
        if type(card)!=Card:
            raise TypeError('Card must be type card')
        if card in self.player_deck:
            return 'Card is already in player deck'
        self.player_deck.append(card)
