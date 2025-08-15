// Inglês Autodidata - JavaScript Functionality

document.addEventListener('DOMContentLoaded', function() {
    console.log('🇺🇸 Welcome to Inglês Autodidata!');
    
    // Add welcome message
    displayWelcomeMessage();
    
    // Add click interactions to feature cards
    setupFeatureCards();
});

function displayWelcomeMessage() {
    const welcomeSection = document.querySelector('.welcome');
    if (welcomeSection) {
        welcomeSection.addEventListener('click', function() {
            alert('Welcome to your English learning journey! 🎓\n\nThis is just the beginning. More features coming soon!');
        });
    }
}

function setupFeatureCards() {
    const featureCards = document.querySelectorAll('.feature-card');
    
    featureCards.forEach(card => {
        card.addEventListener('click', function() {
            const featureTitle = this.querySelector('h3').textContent;
            
            let message = '';
            if (featureTitle.includes('Lessons')) {
                message = '📚 Lessons feature coming soon!\n\nYou will be able to access structured English lessons here.';
            } else if (featureTitle.includes('Vocabulary')) {
                message = '💭 Vocabulary builder coming soon!\n\nExpand your English vocabulary with interactive word games.';
            } else if (featureTitle.includes('Practice')) {
                message = '🎯 Practice exercises coming soon!\n\nTest your knowledge with quizzes and interactive exercises.';
            }
            
            if (message) {
                alert(message);
            }
        });
    });
}

// Utility functions for future development
const InglesAutodidata = {
    version: '1.0.0',
    
    // Placeholder for lesson management
    lessons: [],
    
    // Placeholder for vocabulary management
    vocabulary: [],
    
    // Placeholder for user progress
    userProgress: {
        lessonsCompleted: 0,
        vocabularyLearned: 0,
        practiceScore: 0
    },
    
    // Initialize the app
    init: function() {
        console.log('Initializing Inglês Autodidata v' + this.version);
        // Future initialization code here
    }
};

// Initialize the app
InglesAutodidata.init();
