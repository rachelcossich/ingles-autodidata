#!/usr/bin/env python3
"""
Inglês Autodidata - Self-Taught English Learning App
Main application entry point
"""

import sys
import os
from datetime import datetime
from src.menu_manager import MenuManager
from src.user_manager import UserManager
from src.learning_session import LearningSession
from src.utils import clear_screen, print_banner

def main():
    """Main application function"""
    clear_screen()
    print_banner()
    
    # Initialize user manager
    user_manager = UserManager()
    
    # Check if user exists or create new user
    if not user_manager.has_users():
        print("🎉 Welcome to Inglês Autodidata!")
        print("Let's start your English learning journey!\n")
        user_manager.create_user()
    
    # Login user
    current_user = user_manager.login()
    if not current_user:
        print("❌ Unable to login. Exiting...")
        return
    
    print(f"👋 Welcome back, {current_user['name']}!")
    
    # Initialize menu manager with current user
    menu_manager = MenuManager(current_user, user_manager)
    
    # Start main application loop
    try:
        menu_manager.run()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using Inglês Autodidata!")
        print("Keep practicing and see you soon! 🌟")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the application.")

if __name__ == "__main__":
    main()
