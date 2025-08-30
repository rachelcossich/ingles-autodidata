"""
Grammar Management System for Inglês Autodidata
"""

import json
import os
from typing import List, Dict

class GrammarManager:
    def __init__(self, data_file: str = "data/grammar.json"):
        self.data_file = data_file
        self.grammar_exercises = self._load_exercises()
    
    def _load_exercises(self) -> Dict:
        """Load grammar exercises from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._create_default_exercises()
        return self._create_default_exercises()
    
    def _create_default_exercises(self) -> Dict:
        """Create default grammar exercises"""
        return {
            "verbs": [
                {
                    "question": "I _____ to the store yesterday.",
                    "options": ["go", "went", "going", "goes"],
                    "correct": "went",
                    "explanation": "Use past tense 'went' for actions completed in the past."
                },
                {
                    "question": "She _____ English for five years.",
                    "options": ["studies", "studied", "has studied", "studying"],
                    "correct": "has studied",
                    "explanation": "Use present perfect for actions that started in the past and continue to the present."
                },
                {
                    "question": "They _____ dinner when I called.",
                    "options": ["eat", "ate", "were eating", "have eaten"],
                    "correct": "were eating",
                    "explanation": "Use past continuous for actions in progress at a specific time in the past."
                },
                {
                    "question": "Tomorrow, I _____ my friend at the airport.",
                    "options": ["meet", "met", "will meet", "have met"],
                    "correct": "will meet",
                    "explanation": "Use future tense 'will meet' for actions that will happen in the future."
                }
            ],
            "articles": [
                {
                    "question": "I need _____ pencil to write.",
                    "options": ["a", "an", "the", "no article"],
                    "correct": "a",
                    "explanation": "Use 'a' before consonant sounds (pencil starts with 'p' sound)."
                },
                {
                    "question": "She is _____ engineer.",
                    "options": ["a", "an", "the", "no article"],
                    "correct": "an",
                    "explanation": "Use 'an' before vowel sounds (engineer starts with vowel sound)."
                },
                {
                    "question": "_____ sun rises in the east.",
                    "options": ["A", "An", "The", "No article"],
                    "correct": "The",
                    "explanation": "Use 'the' with unique objects like the sun, moon, earth."
                },
                {
                    "question": "I love _____ music.",
                    "options": ["a", "an", "the", "no article"],
                    "correct": "no article",
                    "explanation": "No article needed with abstract nouns used in general sense."
                }
            ],
            "prepositions": [
                {
                    "question": "The book is _____ the table.",
                    "options": ["on", "in", "at", "by"],
                    "correct": "on",
                    "explanation": "Use 'on' for surfaces (the table surface)."
                },
                {
                    "question": "I will meet you _____ 3 o'clock.",
                    "options": ["on", "in", "at", "by"],
                    "correct": "at",
                    "explanation": "Use 'at' with specific times."
                },
                {
                    "question": "She lives _____ New York.",
                    "options": ["on", "in", "at", "by"],
                    "correct": "in",
                    "explanation": "Use 'in' with cities, countries, and enclosed spaces."
                },
                {
                    "question": "The meeting is _____ Monday.",
                    "options": ["on", "in", "at", "by"],
                    "correct": "on",
                    "explanation": "Use 'on' with days of the week."
                }
            ],
            "questions": [
                {
                    "question": "_____ do you live?",
                    "options": ["What", "Where", "When", "Why"],
                    "correct": "Where",
                    "explanation": "Use 'Where' to ask about location or place."
                },
                {
                    "question": "_____ is your favorite color?",
                    "options": ["What", "Where", "When", "Who"],
                    "correct": "What",
                    "explanation": "Use 'What' to ask about things or information."
                },
                {
                    "question": "_____ are you going to the party?",
                    "options": ["What", "Where", "When", "Why"],
                    "correct": "Why",
                    "explanation": "Use 'Why' to ask about reasons or causes."
                },
                {
                    "question": "_____ will the movie start?",
                    "options": ["What", "Where", "When", "Who"],
                    "correct": "When",
                    "explanation": "Use 'When' to ask about time."
                }
            ],
            "mixed": [
                {
                    "question": "If I _____ rich, I would travel the world.",
                    "options": ["am", "was", "were", "will be"],
                    "correct": "were",
                    "explanation": "Use 'were' in hypothetical situations (second conditional)."
                },
                {
                    "question": "The car _____ by my brother yesterday.",
                    "options": ["repaired", "was repaired", "is repaired", "repairs"],
                    "correct": "was repaired",
                    "explanation": "Use passive voice: 'was repaired' (past tense passive)."
                },
                {
                    "question": "She speaks English _____ than me.",
                    "options": ["good", "better", "best", "well"],
                    "correct": "better",
                    "explanation": "Use comparative form 'better' to compare two people."
                },
                {
                    "question": "I have _____ finished my homework.",
                    "options": ["yet", "already", "still", "ever"],
                    "correct": "already",
                    "explanation": "Use 'already' in positive statements about completed actions."
                }
            ]
        }
    
    def get_exercises_by_topic(self, topic: str) -> List[Dict]:
        """Get grammar exercises by topic"""
        if topic == "mixed":
            # Return exercises from all topics for mixed practice
            all_exercises = []
            for topic_name, exercises in self.grammar_exercises.items():
                if topic_name != "mixed":
                    all_exercises.extend(exercises)
            # Add specific mixed exercises
            all_exercises.extend(self.grammar_exercises.get("mixed", []))
            return all_exercises
        
        return self.grammar_exercises.get(topic, [])
    
    def get_exercises_by_difficulty(self, difficulty: str) -> List[Dict]:
        """Get exercises by difficulty level"""
        # For now, all exercises are general difficulty
        # This can be expanded to include difficulty levels in the data
        all_exercises = []
        for exercises in self.grammar_exercises.values():
            all_exercises.extend(exercises)
        return all_exercises
    
    def add_exercise(self, topic: str, question: str, options: List[str], 
                    correct: str, explanation: str = ""):
        """Add a new grammar exercise"""
        if topic not in self.grammar_exercises:
            self.grammar_exercises[topic] = []
        
        exercise = {
            "question": question,
            "options": options,
            "correct": correct,
            "explanation": explanation
        }
        
        self.grammar_exercises[topic].append(exercise)
        self._save_exercises()
    
    def _save_exercises(self):
        """Save exercises to JSON file"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.grammar_exercises, f, indent=2, ensure_ascii=False)
    
    def get_topics(self) -> List[str]:
        """Get all available grammar topics"""
        return list(self.grammar_exercises.keys())
    
    def get_exercise_count(self, topic: str = None) -> int:
        """Get total exercise count, optionally by topic"""
        if topic:
            return len(self.grammar_exercises.get(topic, []))
        
        total = 0
        for exercises in self.grammar_exercises.values():
            total += len(exercises)
        
        return total
