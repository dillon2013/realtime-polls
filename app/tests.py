import unittest
import main
from tornado.testing import AsyncHTTPTestCase

class testApp(AsyncHTTPTestCase):
    def get_app(self):
        return main.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main()