"""
Learning Session Management for Inglês Autodidata
"""

import time
import random
from typing import Dict, List
from .utils import (
    clear_screen, print_separator, get_user_input, 
    print_colored_text, animate_text, format_score, shuffle_list
)
from .vocabulary_manager import VocabularyManager
from .grammar_manager import GrammarManager
from .conversation_manager import ConversationManager

class LearningSession:
    def __init__(self, user: Dict, user_manager):
        self.user = user
        self.user_manager = user_manager
        self.vocabulary_manager = VocabularyManager()
        self.grammar_manager = GrammarManager()
        self.conversation_manager = ConversationManager()
        
    def start_vocabulary_session(self, difficulty: str):
        """Start a vocabulary learning session"""
        clear_screen()
        print(f"📖 VOCABULARY PRACTICE - {difficulty.upper()}")
        print_separator()
        
        # Get vocabulary words for the session
        words = self.vocabulary_manager.get_words_by_difficulty(difficulty)
        if not words:
            print_colored_text("❌ No vocabulary available for this difficulty level.", "red")
            return
        
        # Shuffle and limit to session size
        session_words = shuffle_list(words)[:10]  # 10 words per session
        
        print(f"📚 Starting vocabulary session with {len(session_words)} words...")
        print("You'll be shown definitions and need to guess the word!")
        input("\\nPress Enter to start...")
        
        # Session tracking
        correct_answers = 0
        total_questions = len(session_words)
        session_start = time.time()
        new_words_learned = 0
        
        for i, word_data in enumerate(session_words, 1):
            clear_screen()
            
            # Show progress
            print(f"📖 VOCABULARY PRACTICE - Question {i}/{total_questions}")
            print_separator()
            
            word = word_data["word"]
            definition = word_data["definition"]
            examples = word_data.get("examples", [])
            
            # Show definition
            print("🎯 DEFINITION:")
            print(f"   {definition}")
            
            if examples:
                print("\\n📝 EXAMPLE:")
                print(f"   {random.choice(examples)}")
            
            print(f"\\n💭 What word matches this definition?")
            
            # Get user answer
            user_answer = get_user_input("Your answer").lower().strip()
            
            # Check answer
            if user_answer == word.lower():
                print_colored_text("✅ Correct! Well done!", "green")
                correct_answers += 1
                new_words_learned += 1
            else:
                print_colored_text(f"❌ Incorrect. The answer was: {word}", "red")
                print(f"💡 Remember: {word} - {definition}")
            
            if i < total_questions:
                input("\\nPress Enter for next question...")
        
        # Session summary
        session_end = time.time()
        session_time = int(session_end - session_start)
        
        self._show_session_summary(
            "Vocabulary",
            correct_answers,
            total_questions,
            session_time,
            new_words_learned,
            difficulty
        )
        
        # Update user stats
        session_stats = {
            "correct": correct_answers,
            "total": total_questions,
            "time_minutes": session_time // 60,
            "new_words": new_words_learned,
            "category": "vocabulary"
        }
        self.user_manager.update_user_stats(self.user, session_stats)
    
    def start_grammar_session(self, topic: str):
        """Start a grammar practice session"""
        clear_screen()
        print(f"📝 GRAMMAR PRACTICE - {topic.upper()}")
        print_separator()
        
        # Get grammar exercises
        exercises = self.grammar_manager.get_exercises_by_topic(topic)
        if not exercises:
            print_colored_text("❌ No grammar exercises available for this topic.", "red")
            return
        
        # Shuffle and limit to session size
        session_exercises = shuffle_list(exercises)[:8]  # 8 exercises per session
        
        print(f"📝 Starting grammar session: {topic}")
        print("You'll complete sentences or choose the correct grammar!")
        input("\\nPress Enter to start...")
        
        # Session tracking
        correct_answers = 0
        total_questions = len(session_exercises)
        session_start = time.time()
        
        for i, exercise in enumerate(session_exercises, 1):
            clear_screen()
            
            # Show progress
            print(f"📝 GRAMMAR PRACTICE - Question {i}/{total_questions}")
            print_separator()
            
            question = exercise["question"]
            options = exercise["options"]
            correct_answer = exercise["correct"]
            explanation = exercise.get("explanation", "")
            
            # Show question
            print("🎯 QUESTION:")
            print(f"   {question}")
            print()
            
            # Show options
            print("📋 OPTIONS:")
            for j, option in enumerate(options, 1):
                print(f"   {j}. {option}")
            
            # Get user answer
            user_choice = get_user_input(f"Choose option (1-{len(options)})", 
                                       [str(i) for i in range(1, len(options) + 1)])
            user_answer = options[int(user_choice) - 1]
            
            # Check answer
            if user_answer == correct_answer:
                print_colored_text("✅ Correct! Great job!", "green")
                correct_answers += 1
            else:
                print_colored_text(f"❌ Incorrect. The correct answer was: {correct_answer}", "red")
            
            if explanation:
                print(f"💡 Explanation: {explanation}")
            
            if i < total_questions:
                input("\\nPress Enter for next question...")
        
        # Session summary
        session_end = time.time()
        session_time = int(session_end - session_start)
        
        self._show_session_summary(
            "Grammar",
            correct_answers,
            total_questions,
            session_time,
            0,  # No new words in grammar
            topic
        )
        
        # Update user stats
        session_stats = {
            "correct": correct_answers,
            "total": total_questions,
            "time_minutes": session_time // 60,
            "new_words": 0,
            "category": "grammar"
        }
        self.user_manager.update_user_stats(self.user, session_stats)
    
    def start_conversation_session(self, scenario: str):
        """Start a conversation practice session"""
        clear_screen()
        print(f"💬 CONVERSATION PRACTICE - {scenario.upper()}")
        print_separator()
        
        # Get conversation scenarios
        conversations = self.conversation_manager.get_conversations_by_scenario(scenario)
        if not conversations:
            print_colored_text("❌ No conversations available for this scenario.", "red")
            return
        
        # Select a conversation
        conversation = random.choice(conversations)
        
        print(f"💬 Scenario: {conversation['title']}")
        print(f"📍 Setting: {conversation['setting']}")
        print("\\nYou'll practice responding in different conversation situations!")
        input("\\nPress Enter to start...")
        
        # Session tracking
        correct_answers = 0
        total_questions = len(conversation["interactions"])
        session_start = time.time()
        
        for i, interaction in enumerate(conversation["interactions"], 1):
            clear_screen()
            
            # Show progress
            print(f"💬 CONVERSATION PRACTICE - Part {i}/{total_questions}")
            print_separator()
            
            situation = interaction["situation"]
            speaker = interaction["speaker"]
            options = interaction["responses"]
            correct_response = interaction["correct"]
            
            # Show conversation context
            print("🎭 SITUATION:")
            print(f"   {situation}")
            print()
            print(f"🗣️  {speaker}:")
            print(f"   \\\"{interaction['prompt']}\\\"")
            print()
            
            # Show response options
            print("💭 HOW DO YOU RESPOND?")
            for j, option in enumerate(options, 1):
                print(f"   {j}. \\\"{option}\\\"")
            
            # Get user choice
            user_choice = get_user_input(f"Choose response (1-{len(options)})", 
                                       [str(i) for i in range(1, len(options) + 1)])
            user_response = options[int(user_choice) - 1]
            
            # Check answer
            if user_response == correct_response:
                print_colored_text("✅ Excellent response! Very natural!", "green")
                correct_answers += 1
            else:
                print_colored_text(f"❌ Good try! A better response would be:", "yellow")
                print(f"   \\\"{correct_response}\\\"")
            
            if interaction.get("explanation"):
                print(f"\\n💡 {interaction['explanation']}")
            
            if i < total_questions:
                input("\\nPress Enter to continue...")
        
        # Session summary
        session_end = time.time()
        session_time = int(session_end - session_start)
        
        self._show_session_summary(
            "Conversation",
            correct_answers,
            total_questions,
            session_time,
            0,  # No new words counted in conversation
            scenario
        )
        
        # Update user stats
        session_stats = {
            "correct": correct_answers,
            "total": total_questions,
            "time_minutes": session_time // 60,
            "new_words": 0,
            "category": "conversation"
        }
        self.user_manager.update_user_stats(self.user, session_stats)
    
    def _show_session_summary(self, session_type: str, correct: int, total: int, 
                             time_seconds: int, new_words: int, topic: str):
        """Show session summary and results"""
        clear_screen()
        print(f"🎯 {session_type.upper()} SESSION COMPLETE!")
        print_separator("=")
        
        # Calculate score
        score_percentage = (correct / total) * 100 if total > 0 else 0
        
        # Show results
        print("📊 SESSION RESULTS:")
        print(f"   🎯 Topic: {topic.title()}")
        print(f"   ✅ Correct Answers: {correct}/{total}")
        print(f"   📈 Score: {format_score(correct, total)}")
        print(f"   ⏱️  Time: {time_seconds // 60}m {time_seconds % 60}s")
        
        if new_words > 0:
            print(f"   📚 New Words Learned: {new_words}")
        
        print()
        
        # Show performance feedback
        if score_percentage >= 90:
            print_colored_text("🌟 Outstanding! You're mastering this!", "green")
        elif score_percentage >= 75:
            print_colored_text("👍 Great job! Keep up the good work!", "green")
        elif score_percentage >= 60:
            print_colored_text("📚 Good effort! Practice makes perfect!", "yellow")
        else:
            print_colored_text("💪 Don't give up! Review and try again!", "yellow")
        
        # Show motivation
        print("\\n💡 STUDY TIP:")
        tips = [
            "Review your mistakes to improve faster!",
            "Practice a little every day for best results!",
            "Try different difficulty levels to challenge yourself!",
            "Focus on topics that match your learning goals!",
            "Don't rush - understanding is more important than speed!"
        ]
        print(f"   {random.choice(tips)}")
        
        print_separator()
        print("🎉 Keep learning and improving your English!")
