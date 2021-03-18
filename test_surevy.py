import unittest
from surey import AnnonymousSurevy

class TestAnnonymousSurvey(unittest.TestCase):
    """Test for the class AnnoymousSurevey"""

    def setUp(self):
        """
        Create a survey and set respones for use in all test methods
        """
        question = "What langues did you first speak?"
        self.my_surey = AnnonymousSurevy(question)
        self.respones = ['English', 'Spanish', 'Madrain']

    def test_surevy(self):
        """Test that a single respone is stored properly"""
        self.my_survey.store_respones(self.respones[0])
        self.assertIn(self.respones[0], self.my_surey.respones)

    def three_respoens(self):
        """Test that three indivual respones are stored properly"""
        for respone in self.respones:
            self.my_survey.store_respones(respone)
        for respone in self.respones:
            self.assertIn(respone, my_surey.respones)

if __name__ == '__main__':
    unittest.main()
