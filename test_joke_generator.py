import unittest
from unittest.mock import patch, MagicMock
from joke_generator import JokeGenerator

class TestJokeGenerator(unittest.TestCase):
    """Unit tests for the JokeGenerator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.generator = JokeGenerator()
    
    def test_joke_generator_initialization(self):
        """Test that JokeGenerator initializes correctly."""
        self.assertIsNotNone(self.generator.session)
        self.assertEqual(len(self.generator.CATEGORIES), 3)
    
    def test_format_joke_single_line(self):
        """Test formatting of single-line jokes."""
        joke_data = {
            "type": "single",
            "joke": "Why did the chicken cross the road?"
        }
        formatted = self.generator.format_joke(joke_data)
        self.assertIn("Why did the chicken cross the road?", formatted)
        self.assertIn("😄", formatted)
    
    def test_format_joke_two_part(self):
        """Test formatting of two-part jokes."""
        joke_data = {
            "type": "twopart",
            "setup": "Why did the chicken cross the road?",
            "delivery": "To get to the other side!"
        }
        formatted = self.generator.format_joke(joke_data)
        self.assertIn("Why did the chicken cross the road?", formatted)
        self.assertIn("To get to the other side!", formatted)
        self.assertIn("🎭", formatted)
    
    def test_format_joke_with_error(self):
        """Test formatting of error responses."""
        joke_data = {"error": "API Error"}
        formatted = self.generator.format_joke(joke_data)
        self.assertIn("API Error", formatted)
        self.assertIn("❌", formatted)
    
    @patch('joke_generator.requests.Session.get')
    def test_get_random_joke_success(self, mock_get):
        """Test successful joke retrieval."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "type": "single",
            "joke": "Test joke"
        }
        mock_get.return_value = mock_response
        
        result = self.generator.get_random_joke()
        self.assertEqual(result["joke"], "Test joke")
    
    @patch('joke_generator.requests.Session.get')
    def test_get_random_joke_timeout(self, mock_get):
        """Test handling of request timeout."""
        mock_get.side_effect = Exception("Timeout")
        result = self.generator.get_random_joke()
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
