from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')
    def test_init_invalid_args(self):
        """testing invalid arguments"""
        with self.assertRaises(TypeError):
            card=Card(10,5)
        with self.assertRaises(TypeError):
            card=Card('King','Diamonds')
        with self.assertRaises(ValueError):
            card=Card(15,'Hearts')
        with self.assertRaises(ValueError):
            card=Card(11,'moshe')

    def test_init_correct_args(self):
        """testing correct agrguments"""
        card=Card(4,'Clubs')
        self.assertTrue(card.value==4)
        self.assertTrue(card.suit=='Clubs')
        self.assertFalse(card.value==5)
        self.assertFalse(card.suit=='Diamonds')

    def test__gt_(self):
        """checking types of string and int and greater situations"""
        card1=Card(5,'Hearts')
        card2=5
        self.assertRaises(TypeError,card1>card2)
        card1=Card(6,'Clubs')
        card2='test'
        self.assertRaises(TypeError,card1>card2)
        card3=Card(13,'Diamonds')
        card4=Card(12,'Hearts')
        self.assertTrue(card3>card4)
        card5=Card(7,'Spades')
        card6=Card(7,'Clubs')
        self.assertTrue(card6>card5)
        card7=Card(3,'Spades')
        card8=Card(4,'Spades')
        self.assertTrue(card8>card7)

    def test_eq_(self):
        """checking types of string and int and equal situations"""
        card1 = Card(5, 'Hearts')
        card2 = 5
        self.assertRaises(TypeError, card1 == card2)
        card1 = Card(6, 'Clubs')
        card2 = 'test'
        self.assertRaises(TypeError, card1 == card2)
        card1 = Card(5,'Hearts')
        card2 = Card(5,'Hearts')
        self.assertEqual(card1,card2)
        card1= Card(5,'Hearts')
        card2= Card(5,'Diamonds')
        self.assertNotEqual(card1,card2)
        card1 = Card(6, 'Hearts')
        card2 = Card(5, 'Hearts')
        self.assertNotEqual(card1,card2)