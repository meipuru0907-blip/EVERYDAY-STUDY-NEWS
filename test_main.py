import unittest
import requests

class TestRSSFeed(unittest.TestCase):
    def test_rss_feed(self):
        url = 'http://example.com/rss'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<?xml', response.text)

class TestGeminiAPI(unittest.TestCase):
    def test_gemini_api(self):
        url = 'https://api.gemini.com/v1/pubticker/btcusd'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('last', response.json())

class TestLINEMessaging(unittest.TestCase):
    def test_send_message(self):
        url = 'https://api.line.me/v2/bot/message/push'
        headers = {'Authorization': 'Bearer YOUR_CHANNEL_ACCESS_TOKEN'}
        data = {
            'to': 'USER_ID',
            'messages': [{'type': 'text', 'text': 'Hello, world!'}]
        }
        response = requests.post(url, headers=headers, json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()