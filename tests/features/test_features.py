import unittest
import app.api.base.base_name as names
import requests as req
from app.config.config import HOST


class TestFeatures(unittest.TestCase):
    def test_get_features(self):
        r = req.get(HOST + '/api/features/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)


if __name__ == '__main__':
    unittest.main()
