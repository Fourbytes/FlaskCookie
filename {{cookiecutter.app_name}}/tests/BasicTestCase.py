import unittest
import tempfile
import os

from webapp import app, db


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        rv = self.app.get('/')
        assert 'Hello' in rv.data.decode()
