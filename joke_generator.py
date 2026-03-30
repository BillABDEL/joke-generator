import requests
import random
from typing import Dict, Optional

class JokeGenerator:
    """A random joke generator using the JokeAPI external API."""
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    CATEGORIES = ["General", "Programming", "Knock-Knock"]
    
    def __init__(self):
        self.session = requests.Session()
    
    def get_random_joke(self, category: Optional[str] = None, safe_mode: bool = True) -> Dict:
        """
        Fetch a random joke from the JokeAPI.
        
        Args:
            category: Joke category (General, Programming, Knock-Knock). 
                     If None, uses a random category.
            safe_mode: If True, filters out offensive jokes.
        
        Returns:
            Dictionary containing the joke data.
        """
        if category is None:
            category = random.choice(self.CATEGORIES)
        
        # Build query parameters
        params = {}
        if safe_mode:
            params["safe-mode"] = "true"
        
        try:
            url = f"{self.BASE_URL}/{category}"
            response = self.session.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("error"):
                return {"error": "Failed to fetch joke. Try again!"}
            
            return data
            
        except requests.exceptions.Timeout:
            return {"error": "Request timed out. Please try again."}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection error. Check your internet connection."}
        except requests.exceptions.RequestException as e:
            return {"error": f"API Error: {str(e)}"}
    
    def format_joke(self, joke_data: Dict) -> str:
        """
        Format joke data into a readable string.
        
        Args:
            joke_data: Dictionary containing joke information.
        
        Returns:
            Formatted joke string.
        """
        if "error" in joke_data:
            return f"❌ {joke_data['error']}"
        
        if joke_data.get("type") == "twopart":
            return f"🎭 {joke_data.get('setup', '')}\n\n😄 {joke_data.get('delivery', '')}"
        else:
            return f"😄 {joke_data.get('joke', '')}"
    
    def get_multiple_jokes(self, count: int = 3, category: Optional[str] = None) -> list:
        """
        Fetch multiple random jokes.
        
        Args:
            count: Number of jokes to fetch.
            category: Joke category (optional).
        
        Returns:
            List of formatted joke strings.
        """
        jokes = []
        for _ in range(count):
            joke_data = self.get_random_joke(category=category)
            formatted = self.format_joke(joke_data)
            jokes.append(formatted)
        
        return jokes
