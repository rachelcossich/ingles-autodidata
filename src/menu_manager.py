"""
Menu Management System for Inglês Autodidata
"""

from typing import Dict
from .utils import (
    clear_screen, print_separator, get_user_input, 
    print_colored_text, pause_for_user, get_difficulty_emoji
)
from .learning_session import LearningSession
from .vocabulary_manager import VocabularyManager

class MenuManager:
    def __init__(self, user: Dict, user_manager):
        self.user = user
        self.user_manager = user_manager
        self.learning_session = LearningSession(user, user_manager)
        self.vocabulary_manager = VocabularyManager()
        
    def run(self):
        """Main menu loop"""
        while True:
            self.show_main_menu()
            choice = self.get_menu_choice()
            
            if choice == "1":
                self.start_vocabulary_practice()
            elif choice == "2":
                self.start_grammar_practice()
            elif choice == "3":
                self.start_conversation_practice()
            elif choice == "4":
                self.show_progress()
            elif choice == "5":
                self.show_profile()
            elif choice == "6":
                self.show_settings()
            elif choice == "7":
                self.show_help()
            elif choice == "8":
                break
            else:
                print_colored_text("❌ Invalid option. Please try again.", "red")
                pause_for_user()
    
    def show_main_menu(self):
        """Display the main menu"""
        clear_screen()
        
        # Show user info
        level_emoji = get_difficulty_emoji(self.user["level"])
        stats = self.user_manager.get_user_stats(self.user)
        
        print(f"👤 {self.user['name']} | {level_emoji} {self.user['level'].title()} | 🔥 {stats['streak_days']} day streak")
        print_separator("=")
        
        print("📚 INGLÊS AUTODIDATA - MAIN MENU")
        print_separator()
        
        print("🎯 LEARNING MODULES:")
        print("1. 📖 Vocabulary Practice")
        print("2. 📝 Grammar Exercises") 
        print("3. 💬 Conversation Practice")
        print()
        
        print("📊 PROGRESS & PROFILE:")
        print("4. 📈 View Progress")
        print("5. 👤 My Profile")
        print("6. ⚙️  Settings")
        print()
        
        print("ℹ️  HELP & EXIT:")
        print("7. ❓ Help")
        print("8. 🚪 Exit")
        
        print_separator()
    
    def get_menu_choice(self) -> str:
        """Get user's menu choice"""
        return get_user_input("Choose an option (1-8)", 
                            [str(i) for i in range(1, 9)])
    
    def start_vocabulary_practice(self):
        """Start vocabulary practice session"""
        clear_screen()
        print("📖 VOCABULARY PRACTICE")
        print_separator()
        
        # Show difficulty options
        print("Choose difficulty level:")
        print("1. 🟢 Beginner (Basic words)")
        print("2. 🟡 Intermediate (Common words)")
        print("3. 🔴 Advanced (Complex words)")
        print("4. 🎯 Adaptive (Based on your level)")
        
        difficulty_choice = get_user_input("Select difficulty (1-4)", ["1", "2", "3", "4"])
        
        difficulty_map = {
            "1": "beginner",
            "2": "intermediate", 
            "3": "advanced",
            "4": self.user["level"]  # Use user's current level
        }
        
        difficulty = difficulty_map[difficulty_choice]
        
        # Start session
        self.learning_session.start_vocabulary_session(difficulty)
        pause_for_user()
    
    def start_grammar_practice(self):
        """Start grammar practice session"""
        clear_screen()
        print("📝 GRAMMAR EXERCISES")
        print_separator()
        
        print("Choose grammar topic:")
        print("1. Verb Tenses")
        print("2. Articles (a, an, the)")
        print("3. Prepositions")
        print("4. Question Formation")
        print("5. Mixed Practice")
        
        topic_choice = get_user_input("Select topic (1-5)", ["1", "2", "3", "4", "5"])
        
        topic_map = {
            "1": "verbs",
            "2": "articles",
            "3": "prepositions", 
            "4": "questions",
            "5": "mixed"
        }
        
        topic = topic_map[topic_choice]
        
        # Start session
        self.learning_session.start_grammar_session(topic)
        pause_for_user()
    
    def start_conversation_practice(self):
        """Start conversation practice session"""
        clear_screen()
        print("💬 CONVERSATION PRACTICE")
        print_separator()
        
        print("Choose conversation scenario:")
        print("1. 🏪 Shopping")
        print("2. 🍽️  Restaurant")
        print("3. ✈️  Travel")
        print("4. 💼 Business")
        print("5. 👥 Small Talk")
        
        scenario_choice = get_user_input("Select scenario (1-5)", ["1", "2", "3", "4", "5"])
        
        scenario_map = {
            "1": "shopping",
            "2": "restaurant",
            "3": "travel",
            "4": "business", 
            "5": "smalltalk"
        }
        
        scenario = scenario_map[scenario_choice]
        
        # Start session
        self.learning_session.start_conversation_session(scenario)
        pause_for_user()
    
    def show_progress(self):
        """Show user progress and statistics"""
        clear_screen()
        print("📈 YOUR PROGRESS")
        print_separator()
        
        stats = self.user_manager.get_user_stats(self.user)
        
        print("📊 OVERALL STATISTICS:")
        print(f"   📚 Total Study Sessions: {stats['total_sessions']}")
        print(f"   📖 Words Learned: {stats['words_learned']}")
        print(f"   🎯 Accuracy: {stats['accuracy']}")
        print(f"   ⏱️  Total Study Time: {stats['study_time']}")
        print(f"   🔥 Current Streak: {stats['streak_days']} days")
        print()
        
        print("🎯 LEARNING GOALS:")
        print(f"   📋 Current Level: {get_difficulty_emoji(stats['level'])} {stats['level'].title()}")
        print(f"   🎯 Goals: {stats['goals']}")
        print()
        
        # Show progress by category
        email = self.user["email"]
        if email in self.user_manager.users:
            progress = self.user_manager.users[email]["progress"]
            
            print("📈 PROGRESS BY CATEGORY:")
            for category, levels in progress.items():
                print(f"   {category.title()}:")
                for level, points in levels.items():
                    emoji = get_difficulty_emoji(level)
                    print(f"     {emoji} {level.title()}: {points} points")
            print()
        
        pause_for_user()
    
    def show_profile(self):
        """Show user profile information"""
        clear_screen()
        print("👤 MY PROFILE")
        print_separator()
        
        print(f"📧 Email: {self.user['email']}")
        print(f"👤 Name: {self.user['name']}")
        print(f"📊 Level: {get_difficulty_emoji(self.user['level'])} {self.user['level'].title()}")
        print(f"🎯 Goals: {', '.join(self.user['goals'])}")
        print(f"📅 Member Since: {self.user['created_at'][:10]}")
        print(f"🕐 Last Login: {self.user['last_login'][:10]}")
        
        print()
        print("Options:")
        print("1. Edit Profile")
        print("2. Back to Main Menu")
        
        choice = get_user_input("Choose option (1-2)", ["1", "2"])
        
        if choice == "1":
            self.edit_profile()
    
    def edit_profile(self):
        """Edit user profile"""
        clear_screen()
        print("✏️  EDIT PROFILE")
        print_separator()
        
        print("What would you like to edit?")
        print("1. Name")
        print("2. English Level")
        print("3. Learning Goals")
        print("4. Cancel")
        
        choice = get_user_input("Choose option (1-4)", ["1", "2", "3", "4"])
        
        if choice == "1":
            new_name = get_user_input("Enter new name")
            self.user["name"] = new_name
            self.user_manager.users[self.user["email"]]["name"] = new_name
            self.user_manager._save_users()
            print_colored_text("✅ Name updated successfully!", "green")
            
        elif choice == "2":
            print("Select new English level:")
            print("1. 🟢 Beginner")
            print("2. 🟡 Intermediate")
            print("3. 🔴 Advanced")
            
            level_choice = get_user_input("Choose level (1-3)", ["1", "2", "3"])
            level_map = {"1": "beginner", "2": "intermediate", "3": "advanced"}
            new_level = level_map[level_choice]
            
            self.user["level"] = new_level
            self.user_manager.users[self.user["email"]]["level"] = new_level
            self.user_manager._save_users()
            print_colored_text("✅ Level updated successfully!", "green")
            
        elif choice == "3":
            print("Select new learning goals (multiple allowed):")
            print("1. Vocabulary building")
            print("2. Grammar improvement")
            print("3. Conversation practice")
            print("4. Business English")
            print("5. Travel English")
            
            goals_input = get_user_input("Enter goal numbers (e.g., 1,3,5)")
            goal_map = {
                "1": "vocabulary",
                "2": "grammar",
                "3": "conversation", 
                "4": "business",
                "5": "travel"
            }
            
            new_goals = []
            for goal_num in goals_input.split(','):
                goal_num = goal_num.strip()
                if goal_num in goal_map:
                    new_goals.append(goal_map[goal_num])
            
            self.user["goals"] = new_goals
            self.user_manager.users[self.user["email"]]["goals"] = new_goals
            self.user_manager._save_users()
            print_colored_text("✅ Goals updated successfully!", "green")
        
        pause_for_user()
    
    def show_settings(self):
        """Show application settings"""
        clear_screen()
        print("⚙️  SETTINGS")
        print_separator()
        
        print("1. Reset Progress")
        print("2. Export Data")
        print("3. Delete Account")
        print("4. Back to Main Menu")
        
        choice = get_user_input("Choose option (1-4)", ["1", "2", "3", "4"])
        
        if choice == "1":
            from .utils import get_yes_no_input
            if get_yes_no_input("⚠️  Are you sure you want to reset all progress?"):
                # Reset user stats
                email = self.user["email"]
                self.user_manager.users[email]["stats"] = {
                    "total_sessions": 0,
                    "words_learned": 0,
                    "correct_answers": 0,
                    "total_answers": 0,
                    "study_time_minutes": 0,
                    "streak_days": 0,
                    "last_study_date": None
                }
                self.user_manager._save_users()
                print_colored_text("✅ Progress reset successfully!", "green")
                
        elif choice == "3":
            from .utils import get_yes_no_input
            if get_yes_no_input("⚠️  Are you sure you want to delete your account?"):
                if get_yes_no_input("⚠️  This action cannot be undone. Continue?"):
                    self.user_manager.delete_user(self.user["email"])
                    print_colored_text("✅ Account deleted. Goodbye!", "green")
                    exit()
        
        pause_for_user()
    
    def show_help(self):
        """Show help information"""
        clear_screen()
        print("❓ HELP")
        print_separator()
        
        print("📚 HOW TO USE INGLÊS AUTODIDATA:")
        print()
        print("🎯 LEARNING MODULES:")
        print("   • Vocabulary Practice: Learn new words with definitions and examples")
        print("   • Grammar Exercises: Practice English grammar rules")
        print("   • Conversation Practice: Simulate real-world conversations")
        print()
        print("📊 PROGRESS TRACKING:")
        print("   • View your statistics and learning progress")
        print("   • Track your daily study streak")
        print("   • Monitor accuracy and improvement over time")
        print()
        print("🎯 DIFFICULTY LEVELS:")
        print("   • 🟢 Beginner: Basic vocabulary and simple grammar")
        print("   • 🟡 Intermediate: Common words and standard grammar")
        print("   • 🔴 Advanced: Complex vocabulary and advanced grammar")
        print()
        print("💡 TIPS FOR EFFECTIVE LEARNING:")
        print("   • Study consistently every day to maintain your streak")
        print("   • Focus on areas that match your learning goals")
        print("   • Review mistakes to improve your accuracy")
        print("   • Practice all modules for balanced learning")
        
        pause_for_user()
