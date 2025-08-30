"""
Vocabulary Management System for Inglês Autodidata
"""

import json
import os
from typing import List, Dict

class VocabularyManager:
    def __init__(self, data_file: str = "data/vocabulary.json"):
        self.data_file = data_file
        self.vocabulary = self._load_vocabulary()
    
    def _load_vocabulary(self) -> Dict:
        """Load vocabulary from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._create_default_vocabulary()
        return self._create_default_vocabulary()
    
    def _create_default_vocabulary(self) -> Dict:
        """Create default vocabulary data"""
        return {
            "beginner": [
                {
                    "word": "hello",
                    "definition": "A greeting used when meeting someone",
                    "pronunciation": "/həˈloʊ/",
                    "examples": [
                        "Hello, how are you today?",
                        "She said hello to everyone at the party."
                    ],
                    "category": "greetings"
                },
                {
                    "word": "book",
                    "definition": "A written or printed work consisting of pages",
                    "pronunciation": "/bʊk/",
                    "examples": [
                        "I'm reading a good book about history.",
                        "Please open your book to page 10."
                    ],
                    "category": "objects"
                },
                {
                    "word": "happy",
                    "definition": "Feeling or showing pleasure or contentment",
                    "pronunciation": "/ˈhæpi/",
                    "examples": [
                        "She looks very happy today.",
                        "I'm happy to help you with this."
                    ],
                    "category": "emotions"
                },
                {
                    "word": "water",
                    "definition": "A clear liquid that forms seas, lakes, rivers, and rain",
                    "pronunciation": "/ˈwɔːtər/",
                    "examples": [
                        "Please drink more water every day.",
                        "The water in the lake is very clear."
                    ],
                    "category": "nature"
                },
                {
                    "word": "house",
                    "definition": "A building where people live",
                    "pronunciation": "/haʊs/",
                    "examples": [
                        "My house has three bedrooms.",
                        "They bought a new house last year."
                    ],
                    "category": "places"
                }
            ],
            "intermediate": [
                {
                    "word": "accomplish",
                    "definition": "To achieve or complete successfully",
                    "pronunciation": "/əˈkʌmplɪʃ/",
                    "examples": [
                        "She accomplished her goal of learning English.",
                        "We need to accomplish this task by Friday."
                    ],
                    "category": "actions"
                },
                {
                    "word": "environment",
                    "definition": "The surroundings or conditions in which something exists",
                    "pronunciation": "/ɪnˈvaɪrənmənt/",
                    "examples": [
                        "We must protect our environment.",
                        "The work environment here is very friendly."
                    ],
                    "category": "nature"
                },
                {
                    "word": "opportunity",
                    "definition": "A chance for advancement or progress",
                    "pronunciation": "/ˌɑːpərˈtuːnəti/",
                    "examples": [
                        "This job offers great opportunities for growth.",
                        "Don't miss this opportunity to learn."
                    ],
                    "category": "abstract"
                },
                {
                    "word": "experience",
                    "definition": "Knowledge or skill gained through practice",
                    "pronunciation": "/ɪkˈspɪriəns/",
                    "examples": [
                        "She has five years of experience in marketing.",
                        "Traveling gives you valuable experience."
                    ],
                    "category": "abstract"
                },
                {
                    "word": "communicate",
                    "definition": "To share or exchange information or ideas",
                    "pronunciation": "/kəˈmjuːnɪkeɪt/",
                    "examples": [
                        "It's important to communicate clearly.",
                        "We communicate through email and phone."
                    ],
                    "category": "actions"
                }
            ],
            "advanced": [
                {
                    "word": "perseverance",
                    "definition": "Persistence in doing something despite difficulty",
                    "pronunciation": "/ˌpɜːrsəˈvɪrəns/",
                    "examples": [
                        "Success requires perseverance and hard work.",
                        "Her perseverance paid off in the end."
                    ],
                    "category": "abstract"
                },
                {
                    "word": "ubiquitous",
                    "definition": "Present, appearing, or found everywhere",
                    "pronunciation": "/juːˈbɪkwɪtəs/",
                    "examples": [
                        "Smartphones have become ubiquitous in modern society.",
                        "Coffee shops are ubiquitous in this neighborhood."
                    ],
                    "category": "descriptive"
                },
                {
                    "word": "paradigm",
                    "definition": "A typical example or pattern of something; a model",
                    "pronunciation": "/ˈpærədaɪm/",
                    "examples": [
                        "The internet created a new paradigm for communication.",
                        "This research challenges the existing paradigm."
                    ],
                    "category": "abstract"
                },
                {
                    "word": "meticulous",
                    "definition": "Showing great attention to detail; very careful",
                    "pronunciation": "/məˈtɪkjələs/",
                    "examples": [
                        "She is meticulous about keeping records.",
                        "The artist's meticulous work impressed everyone."
                    ],
                    "category": "descriptive"
                },
                {
                    "word": "eloquent",
                    "definition": "Fluent or persuasive in speaking or writing",
                    "pronunciation": "/ˈeləkwənt/",
                    "examples": [
                        "The speaker gave an eloquent presentation.",
                        "Her eloquent words moved the audience."
                    ],
                    "category": "descriptive"
                }
            ]
        }
    
    def get_words_by_difficulty(self, difficulty: str) -> List[Dict]:
        """Get words by difficulty level"""
        return self.vocabulary.get(difficulty, [])
    
    def get_words_by_category(self, category: str, difficulty: str = None) -> List[Dict]:
        """Get words by category and optionally by difficulty"""
        words = []
        
        if difficulty:
            level_words = self.vocabulary.get(difficulty, [])
            words = [word for word in level_words if word.get("category") == category]
        else:
            for level in self.vocabulary.values():
                words.extend([word for word in level if word.get("category") == category])
        
        return words
    
    def get_random_words(self, count: int, difficulty: str = None) -> List[Dict]:
        """Get random words, optionally filtered by difficulty"""
        import random
        
        if difficulty:
            words = self.vocabulary.get(difficulty, [])
        else:
            words = []
            for level in self.vocabulary.values():
                words.extend(level)
        
        if len(words) <= count:
            return words
        
        return random.sample(words, count)
    
    def search_words(self, query: str) -> List[Dict]:
        """Search for words containing the query"""
        results = []
        query_lower = query.lower()
        
        for level in self.vocabulary.values():
            for word_data in level:
                if (query_lower in word_data["word"].lower() or 
                    query_lower in word_data["definition"].lower()):
                    results.append(word_data)
        
        return results
    
    def add_word(self, word: str, definition: str, difficulty: str, 
                pronunciation: str = "", examples: List[str] = None, 
                category: str = "general"):
        """Add a new word to the vocabulary"""
        if difficulty not in self.vocabulary:
            self.vocabulary[difficulty] = []
        
        word_data = {
            "word": word,
            "definition": definition,
            "pronunciation": pronunciation,
            "examples": examples or [],
            "category": category
        }
        
        self.vocabulary[difficulty].append(word_data)
        self._save_vocabulary()
    
    def _save_vocabulary(self):
        """Save vocabulary to JSON file"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.vocabulary, f, indent=2, ensure_ascii=False)
    
    def get_categories(self, difficulty: str = None) -> List[str]:
        """Get all available categories"""
        categories = set()
        
        if difficulty:
            words = self.vocabulary.get(difficulty, [])
            categories.update(word.get("category", "general") for word in words)
        else:
            for level in self.vocabulary.values():
                categories.update(word.get("category", "general") for word in level)
        
        return sorted(list(categories))
    
    def get_word_count(self, difficulty: str = None) -> int:
        """Get total word count, optionally by difficulty"""
        if difficulty:
            return len(self.vocabulary.get(difficulty, []))
        
        total = 0
        for level in self.vocabulary.values():
            total += len(level)
        
        return total
