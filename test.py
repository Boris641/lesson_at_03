import unittest
import requests
from unittest.mock import patch, Mock
from Lesson_at_03 import get_cat_image

class TestGetRandomCatImage(unittest.TestCase):

   @patch('requests.get')
   def test_successful_request(self, mock_get):
      # Mocking successful response
      mock_response = Mock()
      mock_response.status_code = 200
      mock_response.json.return_value = [{"url": "https://example.com/cat.jpg"}]
      mock_get.return_value = mock_response

      result = get_cat_image()
      self.assertEqual(result, "https://example.com/cat.jpg")

   @patch('requests.get')
   def test_unsuccessful_request(self, mock_get):
      # Mocking unsuccessful response
      mock_response = Mock()
      mock_response.status_code = 404
      mock_get.return_value = mock_response

      result = get_cat_image()
      self.assertIsNone(result)

   @patch('requests.get')
   def test_request_exception(self, mock_get):
      # Mocking request exception
      mock_get.side_effect = requests.RequestException

      result = get_cat_image()
      self.assertIsNone(result)


if __name__ == '__main__':
   unittest.main()



