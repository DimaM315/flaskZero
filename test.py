import os
import unittest

from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # запускается перед каждым тестом
        self.app = app.test_client()
        self.ctx = app.test_request_context()
        self.ctx.push()

    def tearDown(self):
        # запускается после каждого теста
        self.ctx.pop()

    def test_empty_db(self):
        pass