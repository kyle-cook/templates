import unittest
import speak

class SpeakTests(unittest.TestCase):
    """
    Unit test for the speak library
    """

    def testHello(self):
        self.assertEqual("Hello World!", speak.helloworld())
    def testGoodbye(self):
        self.assertEqual("Goodbye World!", speak.goodbyeworld())

if __name__ == "__main__":
    unittest.main()
