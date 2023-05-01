import unittest
import pytest
import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.obj = user.User()

    def tearDown(self):
        pass

    def test_init(self):
        alex = user.User("Alex", 25)
        self.assertEqual(alex.name, "Alex")
        self.assertEqual(alex.age, 25)

        bob = user.User("Bob")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.age, 35)

        self.assertEqual(self.obj.name, "Bot")
        self.assertEqual(self.obj.age, 35)

    def test_print_all(self):
        self.assertEqual(self.obj.printAll(), "Bot возрастом 35")

    @pytest.mark.slow
    def test_print_to_file(self):
        self.obj.printToFile("text.txt")
        result = self.obj.readFromFile("text.txt")
        self.assertEqual(result, self.obj.printAll())


if __name__ == '__main__':
    unittest.main()