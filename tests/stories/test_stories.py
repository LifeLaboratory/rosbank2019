import unittest
import app.api.base.base_name as names
import requests as req
from app.config.config import HOST


class TestStories(unittest.TestCase):
    def test_stories(self):
        d = {
            names.ID_STORIES: 11,
            names.ID_PROFILE: 1
        }
        r = req.post(HOST + '/api/stories', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_stories_insert(self):
        d = {
            names.ID_USER: 1,
            names.URL: ['https://img1.wbstatic.net/big/new/2350000/2352941-1.jpg',
                        'https://img1.wbstatic.net/big/new/2350000/2352941-1.jpg']
        }
        r = req.post(HOST + '/api/stories/add', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_stories_profile(self):
        r = req.get(HOST + '/api/stories/profile/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_stories_update(self):
            d = {
                names.ID_USER: 1,
                names.URL: ['https://img1.wbstatic.net/big/new/2350000/2352941-1.jpg'],
                names.ID_STORIES: 2
            }
            r = req.post(HOST + '/api/stories/update', json=d)
            print(r.text)
            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(r.text)

    def test_stories_view(self):
        d = {
            names.ID_STORIES: 2,
            names.ID_USER: 1,
            names.STATUS: 'open',
            names.IS_LIKE: True
        }
        r = req.post(HOST + '/api/stories/view', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_stories_list(self):
        r = req.get(HOST + '/api/stories/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_public_stories_list(self):
            d = {
                names.ID_PROFILE: [1, 2, 3],
                names.ID_STORIES: 2
            }
            r = req.post(HOST + '/api/stories', json=d)
            print(r.text)
            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(r.text)

    def test_public_stories(self):
            d = {
                names.ID_PROFILE: 1,
                names.ID_STORIES: 2
            }
            r = req.post(HOST + '/api/stories', json=d)
            print(r.text)
            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(r.text)

    def test_close_stage_open(self):
        d = {
            names.ID_USER: 1,
            names.ID_STORIES: 2,
            names.STATUS: 'open'

        }
        r = req.post(HOST + '/api/stories/view', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_close_stage_view(self):
        d = {
            names.ID_USER: 1,
            names.ID_STORIES: 2,
            names.STATUS: 'view'

        }
        r = req.post(HOST + '/api/stories/view', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_like(self):
        d = {
            names.ID_STORIES: 1,
            names.ID_USER: 1,
            names.IS_LIKE: True
        }
        r = req.post(HOST + '/api/stories/update_status', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_dislike(self):
        d = {
            names.ID_STORIES: 1,
            names.ID_USER: 1,
            names.IS_LIKE: False
        }
        r = req.post(HOST + '/api/stories/update_status', json=d)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)


if __name__ == '__main__':
    unittest.main()
