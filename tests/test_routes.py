import os
import readsapi
import unittest
import tempfile

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, readsapi.app.config['DATABASE'] = tempfile.mkstemp()
        readsapi.app.config['TESTING'] = True
        self.app = readsapi.app.test_client()
        readsapi.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(readsapi.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
