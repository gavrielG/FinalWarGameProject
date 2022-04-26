from unittest import TestCase
from Player import *


class TestPlayer(TestCase):
    def setUp(self):
        self.player4 = Player('gavriel', 15)
        self.deck = DeckOfCards()
        self.player4.set_hand(self.deck)
        print(self.player4.player_deck)

    def test_init_(self):
        with self.assertRaises(TypeError):
            player1=Player(5,24)
        with self.assertRaises(TypeError):
            player2=Player('gavriel','moshe')
        #Testing the card number default
        player3=Player('gavriel')
        self.assertTrue(player3.card_num==26)
        #Testing if card number is above 26
        player3=Player('gavriel',28)
        self.assertTrue(player3.card_num==26)
        #Testing if card number is lower than 10
        player3=Player('gavriel',7)
        self.assertTrue(player3.card_num==26)


    def test_set_hand(self):
        player4=Player('gavriel',15)
        deck=DeckOfCards()
        player4.set_hand(deck)
        #Testing that set hand to 15 cards
        self.assertTrue(len(player4.player_deck)==15)
        #Testing that deck of card reduced by player set hand
        self.assertTrue(len(deck.deck)==37)
        #Testing set hand without deck types
        with self.assertRaises(TypeError):
             player4.set_hand(5)
        with self.assertRaises(TypeError):
             player4.set_hand('deck')
        #Testing the set hand answer is None
        self.assertIsNone(player4.set_hand(deck))
        
        
    # @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(1,'Clubs'))
    # def test_set_hand_mock(self, mock_deal_one):
    #     player5=Player('gavriel',10)
    #     deck=DeckOfCards()
    #     player5.set_hand(deck)
    #     self.assertTrue('Ace of Clubs' in player5.player_deck)


    def test_get_card(self):
        #Getting card with get_card function
        #and checking if it doesnt exist in the player deck list
        #and player deck list reduced by 1
        player4 = Player('gavriel', 26)
        deck = DeckOfCards()
        player4.set_hand(deck)
        a=player4.get_card()
        self.assertNotIn(a,player4.player_deck)
        self.assertTrue(len(player4.player_deck)==25)


    def test_add_card(self):
        #Testing type errors
        with self.assertRaises(TypeError):
            self.player4.add_card(5)
        with self.assertRaises(TypeError):
            self.player4.add_card('gavriel')
        #Adding 5 of Spades to Player deck
        # and try to add it again expecting for string result
        self.player4.add_card(Card(5,'Spades'))
        self.assertEqual(self.player4.add_card(Card(5,'Spades')),'Card is already in player deck')

