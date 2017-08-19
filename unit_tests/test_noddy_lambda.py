import os
import unittest
import subprocess
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

    def test__noddy_lambda__lambda_handler__WillExecuteSuccessfully__WhenInvoked(self):

        path = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(path, os.pardir))

        print(project_root)
        result = subprocess.call(["emulambda",
                                  "noddy_lambda.lambda_handler",
                                  "-",
                                  "-v",
                                  "<",
                                  "noddy_lambda/example.json"])

        self.assertTrue(result)
