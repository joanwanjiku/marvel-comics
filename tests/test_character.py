import unittest
from app.models import Character

class CharacterTest(unittest.TestCase):
    def setUp(self):

        self.new_character = Character(1, 'thor', 'he is amazing', '/hsfhdhgd')
    
    def test_instance(self)
        self.assertTrue(isinstance(self.new_character, Character))