import unittest
from translator import english_to_portuguese, portuguese_to_english

class TestTranslator(unittest.TestCase):
  def test_english_to_portuguese(self):
    self.assertEqual(english_to_portuguese('I'), 'Eu')

  def test_english_to_portuguese_null(self):
    self.assertIsNone(english_to_portuguese())

  def test_portuguese_to_english(self):
    self.assertEqual(portuguese_to_english('Eu'), 'I')

  def test_portuguese_to_english_null(self):
    self.assertIsNone(portuguese_to_english())  

if __name__ == '__main__':
  unittest.main()