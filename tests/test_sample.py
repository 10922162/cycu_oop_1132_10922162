import unittest

class TestSample(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello, World!", "Hello, World!")

if __name__ == '__main__':
    unittest.main()