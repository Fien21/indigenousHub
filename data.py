import random

class GameState:
    def __init__(self):
        self.currentQuest = {
            "name": "Beginner's Journey",
            "target": 10,
            "progress": 0,
            "xpReward": 100
        }
        self.hearts = 3
        self.xp = 0
        self.level = 1
        self.streak = 0
        self.wordsLearned = 0
        self.currentWord = 0
        self.words = []

    def fetch_words(self):
        """Mock function to simulate fetching words from a backend."""
        self.words = [
            {
                "Bla'an Word": "Pasey",
                "Pronunciation": "Pah-sey",
                "English Translation": "Good Morning"
            },
            {
                "Bla'an Word": "Ikwam",
                "Pronunciation": "Ee-kwam",
                "English Translation": "Thank You"
            },
            # Add more words here...
        ]
    
    def load_word(self):
        """Load the current word, and return the word with options."""
        if self.currentWord >= len(self.words):
            self.currentWord = 0

        word = self.words[self.currentWord]
        options = self.generate_options(word)
        return {
            "word_display": {
                "Blaan_word": word["Bla'an Word"],
                "audio_button": f"/get_word_audio?word={word['Bla\'an Word']}",
                "pronunciation": word["Pronunciation"] or "Not available"
            },
            "options": options
        }

    def generate_options(self, current_word):
        """Generate multiple options for word translation."""
        options = [current_word["English Translation"]]
        used_words = set([current_word["English Translation"]])

        while len(options) < 4:
            random_word = random.choice(self.words)
            if random_word["English Translation"] not in used_words:
                options.append(random_word["English Translation"])
                used_words.add(random_word["English Translation"])

        return self.shuffle(options)

    def shuffle(self, array):
        """Shuffle the options list."""
        for i in range(len(array) - 1, 0, -1):
            j = random.randint(0, i)
            array[i], array[j] = array[j], array[i]
        return array

    def check_answer(self, selected_option):
        """Check if the selected answer is correct."""
        word = self.words[self.currentWord]
        correct_answer = word["English Translation"]
        
        if selected_option == correct_answer:
            self.handle_correct_answer()

    def handle_correct_answer(self):
        """Handle actions when the answer is correct."""
        self.xp += self.currentQuest["xpReward"]
        self.level_up()

    def level_up(self):
        """Level up logic."""
        if self.xp >= 100:
            self.level += 1
            self.xp = 0

# Example of using the GameState class

game_state = GameState()
game_state.fetch_words()

# Load the first word
word_data = game_state.load_word()
print("Current Word to Guess: ", word_data['word_display'])

# Simulate answering a question correctly
game_state.check_answer("Good Morning")

# Print out updated game stats
print("XP:", game_state.xp)
print("Level:", game_state.level)
