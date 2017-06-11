from test_plus.test import TestCase


class TestViews(TestCase):

    def testIndex(self):
        response = self.get('/')
        self.response_200(response)
