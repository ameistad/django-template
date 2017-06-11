from test_plus.test import TestCase


class TestAdmin(TestCase):

    def testAdminUrl(self):
        response = self.get('admin:index')
        self.response_302(response)
