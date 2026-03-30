from joke_generator import JokeGenerator
import sys

def main():
    """Main entry point for the joke generator."""
    generator = JokeGenerator()
    
    print("🎭 Welcome to the Random Joke Generator! 🎭\n")
    print("Available commands:")
    print("  1 - Get a random joke")
    print("  2 - Get a joke from a specific category")
    print("  3 - Get multiple jokes")
    print("  4 - List available categories")
    print("  5 - Exit\n")
    
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n⏳ Fetching joke...\n")
            joke = generator.get_random_joke()
            formatted = generator.format_joke(joke)
            print(formatted)
            print("\n" + "-" * 50 + "\n")
        
        elif choice == "2":
            print(f"\nAvailable categories: {', '.join(generator.CATEGORIES)}")
            category = input("Enter category: ").strip()
            
            if category not in generator.CATEGORIES:
                print("❌ Invalid category!\n")
                continue
            
            print("\n⏳ Fetching joke...\n")
            joke = generator.get_random_joke(category=category)
            formatted = generator.format_joke(joke)
            print(formatted)
            print("\n" + "-" * 50 + "\n")
        
        elif choice == "3":
            try:
                count = int(input("How many jokes? (1-10): ").strip())
                if count < 1 or count > 10:
                    print("❌ Please enter a number between 1 and 10!\n")
                    continue
                
                print(f"\n⏳ Fetching {count} jokes...\n")
                jokes = generator.get_multiple_jokes(count=count)
                
                for i, joke in enumerate(jokes, 1):
                    print(f"Joke {i}:\")
                    print(joke)
                    print("\n" + "-" * 50 + "\n")
            
            except ValueError:
                print("❌ Please enter a valid number!\n")
        
        elif choice == "4":
            print(f"\nAvailable categories: {', '.join(generator.CATEGORIES)}\n")
        
        elif choice == "5":
            print("\n👋 Thanks for using the Joke Generator! Goodbye!\n")
            sys.exit(0)
        
        else:
            print("❌ Invalid choice! Please enter 1-5.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)