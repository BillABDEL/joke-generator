````markdown
# Random Joke Generator 🎭

A Python-based random joke generator that fetches jokes from the [JokeAPI](https://jokeapi.dev) external API.

## Features

- 🎲 Fetch random jokes from various categories
- 🎭 Support for multiple joke types (single-line and two-part jokes)
- 🛡️ Safe mode to filter offensive content
- 🔄 Get multiple jokes at once
- 🎯 Category-based joke selection
- ⚡ Error handling and timeout management
- 💬 Interactive CLI interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BillABDELanaconda/joke-generator.git
cd joke-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode (Recommended)

Run the interactive CLI:
```bash
python main.py
```

The program will present a menu with options to:
- Get a random joke
- Get jokes from specific categories (General, Programming, Knock-Knock)
- Fetch multiple jokes at once
- List available categories
- Exit

### Programmatic Usage

Use the `JokeGenerator` class in your own code:

```python
from joke_generator import JokeGenerator

# Create generator instance
generator = JokeGenerator()

# Get a random joke
joke = generator.get_random_joke()
print(generator.format_joke(joke))

# Get a joke from a specific category
joke = generator.get_random_joke(category="Programming")
print(generator.format_joke(joke))

# Get multiple jokes
jokes = generator.get_multiple_jokes(count=5, category="General")
for joke in jokes:
    print(joke)
```

## API Reference

### JokeGenerator Class

#### Methods

**`get_random_joke(category: Optional[str] = None, safe_mode: bool = True) -> Dict`**
- Fetches a random joke from the JokeAPI
- Parameters:
  - `category`: Joke category (General, Programming, Knock-Knock)
  - `safe_mode`: Filter offensive jokes (default: True)
- Returns: Dictionary with joke data or error information

**`format_joke(joke_data: Dict) -> str`**
- Formats joke data into a readable string
- Handles both single-line and two-part jokes
- Parameters:
  - `joke_data`: Dictionary containing joke information
- Returns: Formatted joke string with emojis

**`get_multiple_jokes(count: int = 3, category: Optional[str] = None) -> list`**
- Fetches multiple jokes
- Parameters:
  - `count`: Number of jokes to fetch
  - `category`: Optional category filter
- Returns: List of formatted joke strings

## Examples

### Example 1: Get a random Programming joke
```
$ python main.py
Enter your choice (1-5): 2
Available categories: General, Programming, Knock-Knock
Enter category: Programming
⏳ Fetching joke...
🎭 Why do Java developers wear glasses?
😄 Because they don't C#
```

### Example 2: Get 3 random jokes
```
$ python main.py
Enter your choice (1-5): 3
How many jokes? (1-10): 3
⏳ Fetching 3 jokes...

Joke 1:
😄 Why do programmers prefer dark mode? Because light attracts bugs!
```

## Error Handling

The generator includes robust error handling for:
- Network timeouts
- Connection errors
- Invalid API responses
- Invalid user input

## API Details

This project uses the [JokeAPI](https://jokeapi.dev):
- **Base URL**: `https://v2.jokeapi.dev/joke`
- **Categories**: General, Programming, Knock-Knock
- **Response Format**: JSON
- **Rate Limiting**: No authentication required

## Requirements

- Python 3.7+
- requests library (see requirements.txt)

## License

MIT License - Feel free to use this project for any purpose!

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Troubleshooting

**"Connection error"**: Check your internet connection and API availability.

**"Request timed out"**: The API server may be slow. Try again in a moment.

**"Invalid category"**: Use only: General, Programming, Knock-Knock

## Author

Created with ❤️ by BillABDELanaconda

---

**Have fun with jokes! 😄**
````