from DeckOfCards import DeckOfCards
from unittest import TestCase


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.mydeck = DeckOfCards()
        print(self.mydeck)

    def test__init__(self):
        """"checking the type of deck"""
        self.assertTrue(type(self.mydeck) is DeckOfCards)

    def test_cards_shuffle(self):
        """"shuffling a deck and checking deck after and before shuffling """
        self.mydeck2 = DeckOfCards()
        self.mydeck2.cards_shuffle()
        self.assertNotEqual(self.mydeck, self.mydeck2)

    def test_deal_one(self):
        """Deleting card, checking len of deck and that the card is not in deck"""
        a = DeckOfCards.deal_one(self.mydeck)
        self.assertEqual(len(self.mydeck.deck), 51)
        self.assertNotIn(a, self.mydeck.deck)




