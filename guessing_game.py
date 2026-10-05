import random

def play_game(difficulty):
    """Play a number guessing game based on difficulty level."""
    
    difficulty_settings = {
        "easy": {"max": 50, "hint": "guess between 1-50"},
        "medium": {"max": 100, "hint": "guess between 1-100"},
        "hard": {"max": 500, "hint": "guess between 1-500"}
    }
    
    if difficulty.lower() not in difficulty_settings:
        print("Invalid difficulty. Please enter EASY, MEDIUM, or HARD.")
        return
    
    settings = difficulty_settings[difficulty.lower()]
    max_num = settings["max"]
    hint_text = settings["hint"]
    
    number = random.randint(1, max_num)
    guess = None
    count = 0
    
    print(f"\nStarting {difficulty.upper()} mode - {hint_text}")
    print("-" * 40)
    
    while guess != number:
        try:
            guess = int(input(f"Enter your guess ({hint_text}): "))
            
            if guess < 1 or guess > max_num:
                print(f"Please enter a number between 1 and {max_num}.")
                continue
            
            count += 1
            
            if guess == number:
                print(f"\n🎉 Congratulation! You found the number in {count} step{'s' if count != 1 else ''}!")
            elif number > guess:
                print("Hint: The number is higher than your guess.")
            else:
                print("Hint: The number is lower than your guess.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return count

def main():
    """Main game loop."""
    while True:
        difficulty = input("\nEnter the difficulty you want (EASY, MEDIUM, HARD) or 'QUIT': ").strip()
        
        if difficulty.lower() == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        play_game(difficulty)
        
        again = input("\nDo you want to play again? (YES/NO): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
