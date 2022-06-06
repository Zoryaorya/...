def get_reply(number):
    if number%5==0 and number%3==0:
        return 'FizzBuzz'
    elif number%3==0:
        return 'Fizz'
    elif number%5==0:
        return 'Buzz'
    else:
        return ''

import unittest
import main

class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        number = 6

        result = main.get_reply(number)
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 10

        result = main.get_reply(number)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        number = 15

        result =main.get_reply(number)
        self.assertEqual(result, 'FizzBuzz')


if __name__ == "__main__":
    unittest.main()

