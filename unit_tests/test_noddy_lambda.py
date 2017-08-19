import unittest
from noddy_lambda import lambda_handler


class TestNoddyLambda(unittest.TestCase):

    def test__noddy_lambda__lambda_handler__ReturnsEvent__WhenCalled(self):

        test_event = {
          "key1": "value1",
          "key2": "value2",
          "key3": "value3"
        }

        result = lambda_handler(test_event, {})

        self.assertEqual(test_event, result)
