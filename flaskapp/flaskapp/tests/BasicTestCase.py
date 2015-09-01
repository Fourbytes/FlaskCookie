import unittest

class BasicTestCase(unittest.TestCase):
	def setUp(self):
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		self.app = flaskr.app.test_client()
		flaskr.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flaskr.app.config['DATABASE'])