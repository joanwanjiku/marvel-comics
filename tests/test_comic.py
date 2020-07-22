import unittest
from app.models import Comic

class TestComic(unittest.Testcase):
    def setUp(self):

        self.new_comic = Comic(1, 'marvel 2020', 'amazing looks',20, '/hsfhdhgd')
    
    def test_instance(self)
        self.assertTrue(isinstance(self.new_comic, Comic))