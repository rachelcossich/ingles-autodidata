"""
Utility functions for Inglês Autodidata
"""

import os
import time
import random
from typing import List, Dict

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                     INGLÊS AUTODIDATA                        ║
    ║                  Self-Taught English Learning                ║
    ║                                                              ║
    ║           🇺🇸 Learn English at Your Own Pace 🇬🇧           ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_separator(char="-", length=60):
    """Print a separator line"""
    print(char * length)

def print_colored_text(text: str, color: str = "white"):
    """Print colored text (basic implementation)"""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    
    color_code = colors.get(color.lower(), colors["white"])
    reset_code = colors["reset"]
    print(f"{color_code}{text}{reset_code}")

def get_user_input(prompt: str, valid_options: List[str] = None) -> str:
    """Get user input with validation"""
    while True:
        user_input = input(f"{prompt}: ").strip()
        
        if valid_options:
            if user_input.lower() in [option.lower() for option in valid_options]:
                return user_input.lower()
            else:
                print(f"❌ Please enter one of: {', '.join(valid_options)}")
        else:
            if user_input:
                return user_input
            else:
                print("❌ Please enter a valid input.")

def get_yes_no_input(prompt: str) -> bool:
    """Get yes/no input from user"""
    response = get_user_input(f"{prompt} (y/n)", ["y", "yes", "n", "no"])
    return response in ["y", "yes"]

def pause_for_user():
    """Pause and wait for user to press Enter"""
    input("\nPress Enter to continue...")

def animate_text(text: str, delay: float = 0.03):
    """Animate text character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def format_score(correct: int, total: int) -> str:
    """Format score as percentage"""
    if total == 0:
        return "0%"
    percentage = (correct / total) * 100
    return f"{percentage:.1f}%"

def get_difficulty_emoji(level: str) -> str:
    """Get emoji for difficulty level"""
    emojis = {
        "beginner": "🟢",
        "intermediate": "🟡", 
        "advanced": "🔴"
    }
    return emojis.get(level.lower(), "⚪")

def shuffle_list(items: List) -> List:
    """Shuffle a list and return a new shuffled list"""
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

def format_time_elapsed(seconds: int) -> str:
    """Format elapsed time in readable format"""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds}s"
    else:
        hours = seconds // 3600
        remaining_minutes = (seconds % 3600) // 60
        return f"{hours}h {remaining_minutes}m"

def validate_email(email: str) -> bool:
    """Basic email validation"""
    return "@" in email and "." in email.split("@")[-1]

def create_progress_bar(current: int, total: int, width: int = 50) -> str:
    """Create a progress bar string"""
    if total == 0:
        return "[" + "." * width + "]"
    
    progress = current / total
    filled = int(width * progress)
    bar = "█" * filled + "░" * (width - filled)
    percentage = progress * 100
    
    return f"[{bar}] {percentage:.1f}%"
