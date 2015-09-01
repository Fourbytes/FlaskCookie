import unittest
import tempfile
import os

from {{cookiecutter.app_name}} import app, db


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        rv = self.app.get('/')
        assert 'Hello' in rv.data.decode()