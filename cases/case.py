import unittest
from log  import Log



class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_a(self):
       pass

    Log().debug("shishi ")
    def test_something(self):
       pass
    Log().debug("CESHI ")
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
