"""
User Management System for Inglês Autodidata
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from .utils import get_user_input, get_yes_no_input, validate_email, print_colored_text

class UserManager:
    def __init__(self, data_file: str = "data/users.json"):
        self.data_file = data_file
        self.users = self._load_users()
    
    def _load_users(self) -> Dict:
        """Load users from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
    def _save_users(self):
        """Save users to JSON file"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, indent=2, ensure_ascii=False)
    
    def has_users(self) -> bool:
        """Check if any users exist"""
        return len(self.users) > 0
    
    def create_user(self) -> Dict:
        """Create a new user"""
        print("📝 Creating your profile...")
        print("-" * 30)
        
        # Get user information
        name = get_user_input("Enter your name")
        
        # Get email with validation
        while True:
            email = get_user_input("Enter your email")
            if validate_email(email):
                if email not in self.users:
                    break
                else:
                    print("❌ Email already exists. Please use a different email.")
            else:
                print("❌ Please enter a valid email address.")
        
        # Get learning level
        print("\nSelect your English level:")
        print("1. 🟢 Beginner")
        print("2. 🟡 Intermediate") 
        print("3. 🔴 Advanced")
        
        level_choice = get_user_input("Choose your level (1-3)", ["1", "2", "3"])
        level_map = {"1": "beginner", "2": "intermediate", "3": "advanced"}
        level = level_map[level_choice]
        
        # Get learning goals
        print("\nWhat are your learning goals? (select multiple with commas)")
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
        
        goals = []
        for goal_num in goals_input.split(','):
            goal_num = goal_num.strip()
            if goal_num in goal_map:
                goals.append(goal_map[goal_num])
        
        # Create user object
        user_data = {
            "name": name,
            "email": email,
            "level": level,
            "goals": goals,
            "created_at": datetime.now().isoformat(),
            "last_login": datetime.now().isoformat(),
            "stats": {
                "total_sessions": 0,
                "words_learned": 0,
                "correct_answers": 0,
                "total_answers": 0,
                "study_time_minutes": 0,
                "streak_days": 0,
                "last_study_date": None
            },
            "progress": {
                "vocabulary": {
                    "beginner": 0,
                    "intermediate": 0,
                    "advanced": 0
                },
                "grammar": {
                    "beginner": 0,
                    "intermediate": 0,
                    "advanced": 0
                }
            }
        }
        
        # Save user
        self.users[email] = user_data
        self._save_users()
        
        print_colored_text(f"\n✅ Welcome, {name}! Your profile has been created.", "green")
        return user_data
    
    def login(self) -> Optional[Dict]:
        """Login user"""
        if not self.has_users():
            return None
        
        if len(self.users) == 1:
            # Auto-login if only one user
            email = list(self.users.keys())[0]
            user = self.users[email]
        else:
            # Multiple users - show selection
            print("Select your profile:")
            emails = list(self.users.keys())
            for i, email in enumerate(emails, 1):
                user = self.users[email]
                print(f"{i}. {user['name']} ({email})")
            
            choice = get_user_input(f"Choose profile (1-{len(emails)})", 
                                  [str(i) for i in range(1, len(emails) + 1)])
            email = emails[int(choice) - 1]
            user = self.users[email]
        
        # Update last login
        user["last_login"] = datetime.now().isoformat()
        self._save_users()
        
        return user
    
    def update_user_stats(self, user: Dict, session_stats: Dict):
        """Update user statistics after a learning session"""
        email = user["email"]
        if email not in self.users:
            return
        
        stats = self.users[email]["stats"]
        
        # Update session stats
        stats["total_sessions"] += 1
        stats["correct_answers"] += session_stats.get("correct", 0)
        stats["total_answers"] += session_stats.get("total", 0)
        stats["study_time_minutes"] += session_stats.get("time_minutes", 0)
        stats["words_learned"] += session_stats.get("new_words", 0)
        
        # Update streak
        today = datetime.now().date().isoformat()
        last_study = stats.get("last_study_date")
        
        if last_study == today:
            # Already studied today, keep streak
            pass
        elif last_study is None:
            # First time studying
            stats["streak_days"] = 1
        else:
            from datetime import date, timedelta
            last_date = datetime.fromisoformat(last_study).date()
            today_date = datetime.now().date()
            
            if today_date - last_date == timedelta(days=1):
                # Consecutive day
                stats["streak_days"] += 1
            else:
                # Streak broken
                stats["streak_days"] = 1
        
        stats["last_study_date"] = today
        
        # Update progress based on session type and performance
        if session_stats.get("category"):
            category = session_stats["category"]
            level = user["level"]
            
            if category in self.users[email]["progress"]:
                current_progress = self.users[email]["progress"][category][level]
                points_earned = session_stats.get("correct", 0)
                self.users[email]["progress"][category][level] = current_progress + points_earned
        
        self._save_users()
    
    def get_user_stats(self, user: Dict) -> Dict:
        """Get formatted user statistics"""
        email = user["email"]
        if email not in self.users:
            return {}
        
        stats = self.users[email]["stats"]
        
        # Calculate accuracy
        accuracy = 0
        if stats["total_answers"] > 0:
            accuracy = (stats["correct_answers"] / stats["total_answers"]) * 100
        
        return {
            "total_sessions": stats["total_sessions"],
            "words_learned": stats["words_learned"],
            "accuracy": f"{accuracy:.1f}%",
            "study_time": f"{stats['study_time_minutes']} minutes",
            "streak_days": stats["streak_days"],
            "level": user["level"],
            "goals": ", ".join(user["goals"])
        }
    
    def delete_user(self, email: str) -> bool:
        """Delete a user"""
        if email in self.users:
            del self.users[email]
            self._save_users()
            return True
        return False
