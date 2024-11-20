from data_preprocessing import DataPreprocessing
from train_model import TrainModel
from evaluate_model import EvaluateModel

class GameState:
    def __init__(self):
        self.data_prep = DataPreprocessing()
        self.model = None
        self.train_model_instance = None

    def setup_game(self, file_path):
        """Set up the game by preparing data and training the model."""
        words = self.data_prep.fetch_words(file_path)
        bla_words, translations = self.data_prep.prepare_data()

        # Train the model
        self.train_model_instance = TrainModel(bla_words, translations)
        self.train_model_instance.train()
        self.model = self.train_model_instance

    def evaluate(self, test_words):
        """Evaluate the model with a set of test words."""
        evaluator = EvaluateModel(self.train_model_instance)
        evaluator.evaluate(test_words)

# Example usage
if __name__ == "__main__":
    file_path = r"Datasets\Book1BLaan.csv"  # Specify the CSV file path
    game_state = GameState()
    game_state.setup_game(file_path)

    # Test predictions
    test_words = ["Pasey", "Ikwam", "Kapya"]
    game_state.evaluate(test_words)
