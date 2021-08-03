import unittest
import main as prog

class TestMyVisitors(unittest.TestCase):

    def test_topCountry(self):
        v = prog.Visitors()
        top = v.top
        self.assertEqual(top, "")

if __name__ == '__main__':
    unittest.main()
